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


class ParkCount (Screen):

    totalParks = ObjectProperty(None)
    def on_pre_enter(self):
        self.getInfo()

    def addInfo(self):

        db = globals.client["MainData"]
        my_collection = db["Account Info"]

        updateID = my_collection.find({'name': globals.username}).limit(1)[0]        

        self.Parks = int(self.ids.Submit2.text)
        self.totalParks = self.Parks + updateID['Parks']

        query_filter = {'name': globals.username}
        update_values = {'$set': {'Parks': self.totalParks}}

        result = my_collection.update_one(query_filter, update_values)


        db = globals.client["CollectiveImpact"]
        collection = db["TotalParks"]

        updateID = collection.find({'FindDoc': 'Found'}).limit(1)[0]

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
        db = globals.client["CollectiveImpact"]    
        my_collection = db["TotalParks"]

        updateID = my_collection.find({'FindDoc': 'Found'}).limit(1)[0]

        self.totalParks = updateID['Total']

        notification.notify(title = 'EnviroScope', message = 'The total park count is ' + str(self.totalParks))