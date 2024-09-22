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
import globals

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

class ViewContact(Screen):
    Phone1 = StringProperty("Default Info")
    Address1 = StringProperty("Default Info")
    Role1 = StringProperty("Default Info")

    Phone2 = StringProperty("Default Info")
    Address2 = StringProperty("Default Info")
    Role2 = StringProperty("Default Info")

    Phone3 = StringProperty("Default Info")
    Address3 = StringProperty("Default Info")
    Role3 = StringProperty("Default Info")
    
    def on_pre_enter(self):
        db = globals.client['Contacts']
        collection = db['Info']
        
        cursor = collection.find({"State": globals.state}).limit(2)
    
        stateInfo = list(cursor)
        print(stateInfo)
        print("Querying for state:", globals.state)
        print("State Info Results:", stateInfo)
    
        Person1 = stateInfo[0]
        self.Role1 = Person1['Role']
        self.Address1 = Person1['Address']
        self.Phone1 = Person1['Phone']

        Person2 = stateInfo[1]
        self.Role2 = Person2['Role']
        self.Address2 = Person2['Address']
        self.Phone2 = Person2['Phone']



        cursor = collection.find({"District": globals.district}).limit(1)
        districtInfo = list(cursor)
        Person3 = districtInfo[0]
        self.Role3 = Person3['Role']
        self.Address3 = Person3['Address']
        self.Phone3 = Person3['Phone']