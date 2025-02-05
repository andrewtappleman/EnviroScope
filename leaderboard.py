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

class LeaderBoard (Screen):
    First = StringProperty("Not Enough People")
    FirstCount = ObjectProperty(0)
    Total1 = StringProperty("Not Enough Data")
        
    Second = StringProperty("Not Enough People")
    SecondCount = ObjectProperty(0)
    Total2 = StringProperty("Not Enough Data")
        
    Third = StringProperty("Not Enough People")
    ThirdCount = ObjectProperty(0)
    Total3 = StringProperty("Not Enough Data")
        
    Fourth = StringProperty("Not Enough People")
    FourthCount = ObjectProperty(0)
    Total4 = StringProperty("Not Enough Data")

    Fifth = StringProperty("Not Enough People")
    FifthCount = ObjectProperty(0)
    Total5 = StringProperty("Not Enough Data")

    def on_pre_enter(self):
        db = globals.client['MainData']
        collection = db['Account Info']

        TestFind1 = collection.find().sort('Bottles', -1).limit(1)[0]

        self.First = TestFind1['name']
        self.FirstCount = TestFind1['Bottles']
        self.Total1 = self.First + ', ' + str(self.FirstCount) + ' Litter'

        TestFind2 = collection.find().sort('Bottles', -1).skip(2).limit(1)[0]
        
        self.Second = TestFind2['name']
        self.SecondCount = TestFind2['Bottles']
        self.Total2 = self.Second + ', ' + str(self.SecondCount) + ' Litter'

        TestFind3 = collection.find().sort('Bottles', -1).skip(3).limit(1)[0]
        
        self.Third = TestFind3['name']
        self.ThirdCount = TestFind3['Bottles']
        self.Total3 = self.Third + ', ' + str(self.ThirdCount) + ' Litter'

        TestFind4 = collection.find().sort('Bottles', -1).skip(3).limit(1)[0]

        self.Fourth = TestFind4['name']
        self.FourthCount = TestFind4['Bottles']
        self.Total4 = self.Fourth +  ', ' + str(self.FourthCount) + ' Litter'

        TestFind5 = collection.find().sort('Bottles', -1).skip(5).limit(1)[0]

        self.Fifth = TestFind5['name']
        self.FifthCount = TestFind5['Bottles']
        self.Total5 = self.Fifth + ', ' + str(self.FifthCount) + ' Litter'