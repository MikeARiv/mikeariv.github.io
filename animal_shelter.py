from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        #Update localhost port as required to your port
        self.client = MongoClient('mongodb://localhost:[enter your port number]')
        
        
        #Utilizes the local port for logon along with a username and password defined in fidofinder.ipynb.  Remove # for utilization
        #self.client = MongoClient('mongodb://%s:%s@localhost:[enter your port number]/?authMechanism=DEFAULT&authSource=AAC'%(username,password))
        
        #initiates use of the AAC database in order to see the animals collection
        self.database = self.client['AAC']

# Function to create a new animal object in the database.
    def create(self, data):
        if data is not None:
            return self.database.animals.insert(data)  # data should be dictionary
            #return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
            
# Function to read all animals in the database.
    def read_all (self, data):
        cursor = self.database.animals.find(data,{'_id' : False})
        return cursor
    
    def read(self, data):
        return self.database.animals.find_one(data)

# Function to update all animals in the database.  Remove # from all lines to utilize
    #def update(self, find=dict(), replace=dict()):
        #if find is not None:
        #toUpdate = self.database.animals.update_many(find, {"$set":replace})
        #return json.dumps(str(toUpdate.modified_count) + ' record has been updated')
    #else:
        #raise Exception("Did not work")
          
# Function to delete all animals in the database.  Remove # from all lines to utilize
    #def delete(self, data=dict()):
        #if data is not None:
        #return json.dumps(self.database.animals.remove(data))
   # else:
        #raise Exception("Did not work")
