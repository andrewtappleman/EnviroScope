import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


username = ''
district = ''
state = ''
username = ''
notifLimit = 0
new = 0
Parks = 0
Bottles = 0
uri = "mongodb+srv://admin:admin@enviroscopecluster0.qdwjcoq.mongodb.net/?appName=EnviroScopeCluster0"
# Create a new client and connect to the server
clientel = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    clientel.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
client = clientel