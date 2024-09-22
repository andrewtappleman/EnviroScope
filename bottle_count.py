
#:import webbrowser webbrowser

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
import globals

class BottleCount (Screen):

    def check_account(self):
        
        db = globals.client['BottleCountInfo']
        collection = db['TotalBottles']
        
        Total_Bottles = self.ids.TotalBottles1.text

        globals.Bottles = self.ids.TotalBottle1.text
        
        query = {"Bottles": Total_Bottles}
        
        if self.check_for_type(collection, query):
            self.manager.current = "EnvironmentalIssues"
        else:
            notification.notify(title = 'EnviroScope', message = 'Bottle count was not sucseful in updating')
            self.ids.TotalBottles1.text = ""


    def check_for_type(self, collection, query):
        result = collection.find_one(query)
        return result is not None



    TotalBottles = StringProperty("5")
    def addInfo(self):

        db = globals.client["CollectiveImpact"]
        
        my_collection = db["TotalBottles"]
        data = self.ids.EnterHere2.text
        NameData = [{"Bottles": data}]

        self.Bottles = self.ids.EnterHere2.text

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
        db = globals.client["CollectiveImpact"]
        
        my_collection = db["TotalBottles"]
        self.TotalBottles = -1
        #Purpose is to get the numebr of bottles
        x = 0
        while self.TotalBottles == -1:
            if my_collection.find({'Bottles': str(x)}) == True:
                self.TotalBottles = my_collection.find({'Bottles': str(x)})