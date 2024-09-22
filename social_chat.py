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

class SocialChat(Screen):
    Entry1 = StringProperty('Default Text')
    Entry2 = StringProperty('Default Text')
    Entry3 = StringProperty('Default Text')
    Entry4 = StringProperty('Default Text')
    Entry5 = StringProperty('Default Text')

    Name1 = StringProperty('Default Text')
    Name2 = StringProperty('Default Text')
    Name3 = StringProperty('Default Text')
    Name4 = StringProperty('Default Text')
    Name5 = StringProperty('Default Text')

    def on_enter(self):
        self.refresh()
    def refresh(self):

        db = globals.client['MainData']
        collection = db['Chat']
        EntryFind1 = collection.find().sort('_id', -1).skip(4).limit(1)[0]
        EntryFind2 = collection.find().sort('_id', -1).skip(3).limit(1)[0]
        EntryFind3 = collection.find().sort('_id', -1).skip(2).limit(1)[0]
        EntryFind4 = collection.find().sort('_id', -1).skip(1).limit(1)[0]
        EntryFind5 = collection.find().sort('_id', -1).limit(1)[0]

        self.Entry1 = EntryFind1['Entry']
        self.Name1 = EntryFind1['Username']
        self.Entry2 = EntryFind2['Entry']
        self.Name2 = EntryFind2['Username']
        self.Entry3 = EntryFind3['Entry']
        self.Name3 = EntryFind3['Username']
        self.Entry4 = EntryFind4['Entry']
        self.Name4 = EntryFind4['Username']
        self.Entry5 = EntryFind5['Entry']
        self.Name5 = EntryFind5['Username']
    
    def addToDB(self):

        db = globals.client['MainData']
        collection = db['Chat']
        FullEntry = self.ids.EntryInput.text

        query = [{"Username": globals.username, "Entry": FullEntry}]
        
        try:
            result = collection.insert_many(query)
        except pymongo.errors.OperationFailure:
            print("An authentication error was received. Check your database user permissions.")
            print('')
            print('')
            sys.exit(1)
        else:
            inserted_count = len(result.inserted_ids)
            print("I inserted %d documents." % inserted_count)
            print("")
            print('')
        self.refresh()
