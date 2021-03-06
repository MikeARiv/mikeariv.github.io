'''
Utilization script to allow CRUD operations in MongoDB.
If running on your local system, utilize localhost.
If running on another server, this would require IP and port information accrodingly.
Comments identify items to change.
Additional functionality to create a new collection and find items added.
'''

from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class "Replace with your Database Info" (object):
    """ CRUD operations in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        username = urllib.parse.quote_plus('user')
        user = 'enter username'
        password = urllib.parse.quote_plus('pass/word')
        password = 'enter password'
        #adjust local host or port information to you host device for MongoDB
        self.client = MongoClient('mongodb://%s:%s@localhost:"enter your local port information"' % (user, password))
        self.database = self.client['enter database to use']
        #return True
        
        '''
        additional functionality to create a new collection:
        collection_name = dbname["item_1"]
        
        additional functionality for find an item:
        item_dteails = collection_name.find()
        '''
        
# Complete this create user accounts in MongoDB.
    def create(self, data):
        if data is not None:
            self.database."replace with your databse name".insert(data)  # data should be dictionary
            #We can also insert many with the below inputs
            #collection_name.insert_many([item_1, item_2])
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Ability to read a query in MongoDB for finding one of a data type you are looking for.
    def read(self,data):
        if data is not None:
            return self.database."replace with your databse name".find_one(data)
        else:
            print('Nothing to read, because data parameter is empty')
        return False
        
#Update method for updating a record in your MongoDB
  def update(self, find=dict(), replace=dict()): #utilized to find and replace items
    if find is not None: #if function performing find and replace
        toUpdate = self.database."replace with your databse name".update_many(find, {"$set":replace})
        return json.dumps(str(toUpdate.modified_count) + ' record has been updated')
    else:
        raise Exception("Did not work")
          
  #Delete method to delete a record
  def delete(self, data=dict()):
    if data is not None:
        return json.dumps(self.database."replace with your databse name".remove(data))
    else:
        raise Exception("Did not work")
