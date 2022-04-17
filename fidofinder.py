from jupyter_plotly_dash import JupyterDash

import dash
import dash_leaflet as dl
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
from dash.dependencies import Input, Output
import base64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

#### FIX ME #####
# change animal_shelter and AnimalShelter to match your CRUD Python module file name and class name
from animal_shelter import AnimalShelter

###########################
# Data Manipulation / Model
###########################
# FIX ME update with your username and password and CRUD Python module name

username = "aacuser"
password = "Password#1234"
shelter = AnimalShelter(username, password)

# class read method must support return of cursor object and accept projection json input
df = pd.DataFrame.from_records(shelter.read_all({}))

#########################
# Dashboard Layout / View
#########################
app = JupyterDash('SimpleExample')

#Imprint of Logo
image_filename = 'GraziosoSalvareLogo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#Develop web layout
app.layout = html.Div([
    html.Div(id='hidden-div', style={'display':'none'}),
    html.Center(html.B(html.H1('SNHU CS-340 Dashboard | Michael Rivera'))),
    html.Hr(),
    html.Center(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))),
    html.Hr(),
    html.Div([
        html.Center(html.Label(['Rescue Type Filter Selection'], style={'font-weight': 'bold'})),
        #Development of radio items for selection between rescue types
        html.Center(dcc.RadioItems(
            id='radio-items',
            options=[
                {'label': 'Water Rescue', 'value': 'Filter by Water Rescue'},
                {'label': 'Mountain Rescue', 'value': 'Filter by Mountain Rescue'},
                {'label': 'Disaster Rescue', 'value': 'Filter by Disaster Rescue'},
                {'label': 'Reset', 'value': 'Remove all filters'}
            ],
            value='Filter table by rescue dog types',
            inputStyle={"margin-left": "20px"},
            labelStyle={'display': 'inline-block'}
        ))
    ]),
    html.Br(),
#Create interactive data table
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="custom",
        sort_mode="multi",
        sort_by=[],
        column_selectable=False,
        row_selectable="single",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),
    html.Br(),
    html.Hr(),
    
    html.Div(className='row',
             style={'display': 'flex', "width": "500"},
             children=[
                 html.Div(
                     className='row',
                     style={'display': 'flex'},
                     children=[
                         # where the pie chart will go
                         dcc.Graph(
                             id='graph-id',
                         ),
                         # where the map will go
                         html.Div(
                             id='map-id',
                             className='col s12 m6',
                         ),
                     ]
                 ),
             ])
])

#############################################
# Interaction Between Components / Controller
#############################################

@app.callback(
    Output('datatable-interactivity', 'data'),
    [Input(component_id='radio-items', component_property='value')
     ])
     
#Utilization of radio buttons to return water rescue dogs
def radioFilter(radio_options):
    if radio_options == 'Filter by Water Rescue':
        df = pd.DataFrame.from_records(shelter.findDocs({'animal_type': 'Dog'})).drop(['_id', ''], axis=1)
        df = df.loc[(df['breed'] == 'Labrador Retriever Mix') |
                      (df['breed'] == 'Chesapeake Bay Retriever') |
                      (df['breed'] == 'Newfoundland')]
        df = df.loc[(df['sex_upon_outcome'] == 'Intact Female')]
        df = df.query('26 <= age_upon_outcome_in_weeks <= 156')

    elif radio_options == 'Filter by Mountain Rescue':
        df = pd.DataFrame.from_records(shelter.findDocs({'animal_type': 'Dog'})).drop(['_id', ''], axis=1)
        df = df.loc[(df['breed'] == 'German Shepherd') |
                      (df['breed'] == 'Alaskan Malamute') |
                      (df['breed'] == 'Old English Sheepdog') |
                      (df['breed'] == 'Siberian Husky') |
                      (df['breed'] == 'Rottweiler')]
        df = df.loc[(df['sex_upon_outcome'] == 'Intact Male')]
        df = df.query('26 <= age_upon_outcome_in_weeks <= 156')

    elif radio_options == 'Filter by Disaster Rescue':
        df = pd.DataFrame.from_records(shelter.findDocs({})).drop(['_id', ''], axis=1)
        df = df.loc[(df['breed'] == 'German Shepherd') |
                      (df['breed'] == 'Doberman Pinscher') |
                      (df['breed'] == 'Golden Retriever') |
                      (df['breed'] == 'Bloodhound') |
                      (df['breed'] == 'Rottweiler')]
        df = df.loc[(df['sex_upon_outcome'] == 'Intact Male')]
        df = df.query('20 <= age_upon_outcome_in_weeks <= 300')

    else:
        df = pd.DataFrame.from_records(shelter.findDocs({})).drop(['_id', ''], axis=1)

    return df.to_dict('records')
    
@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    [Input('datatable-interactivity', 'selected_rows')]
)

#Highlights selected row
def update_styles(selected_rows):
    return [{
        'if': { 'row_index': i },
        'background_color': '#8B0000'
    } for i in selected_rows]


@app.callback(
    Output('graph-id', "figure"),
    [Input('datatable-interactivity', "derived_virtual_data")])
    
#Pie Chart integration showing the different outcome types
def update_graph(allData):
    df = pd.DataFrame(allData)

    piechart = px.pie(
        data_frame=df,
        names=df['outcome_type'],
        color_discrete_sequence=px.colors.sequential.RdBu,
    )
    return piechart

#Geolocation chart of all animals
fig = px.scatter_mapbox(df, lat="location_lat", lon="location_long", hover_name="name", hover_data=["breed","date_of_birth"],
                        color_discrete_sequence=["fuchsia"], zoom=5, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

app