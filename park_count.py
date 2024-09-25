from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage
from plyer import notification
from kivy.uix.filechooser import FileChooserIconView
from kivy.lang import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.properties import StringProperty
from kivy.clock import Clock
from pymongo.mongo_client import MongoClient
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.dropdown  import DropDown
from kivy.core.image import Image as CoreImage
from io import BytesIO
from io import BytesIO
from PIL import Image as PILImage
import os
import time
os.environ["PAFY_BACKEND"] = "internal"
import pafy

Builder.load.file('Park Count')

from win10toast import ToastNotifier
from httpx import HTTPStatusError
from kivy.utils import platform
from kivy.clock import Clock
from datetime import datetime, timedelta
import pandas as pd
import json
import os
import webbrowser
import time
os.environ["PAFY_BACKEND"] = "internal"
import pafy
import httpx
import pymongo
import sys
import base64
from pymongo.server_api import ServerApi
import random

uri = "mongodb+srv://admin:admin@enviroscopecluster0.qdwjcoq.mongodb.net/?appName=EnviroScopeCluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

width_base = 15
height_base = 25
scale = 30
Window.size = (width_base * scale, height_base * scale)
username = ''
username = ''
district = ''
state = ''
username = ''
notifLimit = 0
new = 0


class ParkCount(Screen):

    TotalParks = StringProperty("5")
    def addInfo(self):

        global client
        db = client["Main data"]
        
        my_collection = db["Account Info"]
        data = self.ids.Submit2.text
        NameData = [{"Parks": data}]

        global Parks
        self.Parks = self.ids.Submit2.text

        try:
            result = my_collection.insert_many(NameData)
        except pymongo.errors.OperationFailure:
            print("An authentication error was received. Check your database user permissions.")
            sys.exit(1)
        else:
            inserted_count = len(result.inserted_ids)
            print("I inserted %d documents." % inserted_count)
            print("\n")
        self.manager.current = 'EnvironmentalIssues'
    def getInfo(self):
        global client
        db = client["Main data"]
        
        my_collection = db["TotalParks"]
        self.TotalParks = -1
        #Purpose is to get the numebr of bottles
        x = 0
        while self.TotalParks == -1:
            if my_collection.find({'Parks': str(x)}) == True:
                self.TotalParkss = my_collection.find({'Parks': str(x)})
class EnviroScopeApp(App):
    def build(self):
        sm.add_widget(ParkCount(name= 'ParkCount'))
        return sm
if __name__ == '__main__'
    EnviroScope().run()