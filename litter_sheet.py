
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

class LitterSheet (Screen):
    def on_enter(self):
        self.ids.NameInput.text = globals.username
        self.create_dropdown()

    def create_dropdown(self):

        db = globals.client['MainData']
        collection = db['Litter Cleanups']

        dropButton = self.ids.dropButton
    
        dropdown = DropDown(size_hint=(None, None), size=(45 * 8, 75))
    

        options = collection.find({}, {"_id": 0, "Location": 1})
    
        for option in options:
            btn = Button(text=option['Location'], size_hint_y=None, height=44)

            btn = Button(text=option['Location'], size_hint_y=None, height=44, background_color = (0.4196, 0.7922, 0.9569, 1))

            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
    
        dropButton.bind(on_press=dropdown.open)
    
        dropdown.bind(on_select=lambda instance, x: setattr(dropButton, 'text', x))

    def addToList(self):
        
        notification.notify(title = 'EnviroScope', message = 'You have joined a clean up.')

        db = globals.client['MainData']
        collection = db['Jobs Taken']
        
        name = self.ids.NameInput.text
        cleanup = self.ids.dropButton.text
        
        query = [{"Name": name, "Location": cleanup}]
        
        try:
            result = collection.insert_many(query)
        except pymongo.errors.OperationFailure:
            print("An authentication error was received. Check your database user permissions.")
            sys.exit(1)
        else:
            inserted_count = len(result.inserted_ids)
            print("I inserted %d documents." % inserted_count)
            print("\n")