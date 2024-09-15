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

class GetInContact (Screen):
    def on_pre_enter(self):
        self.createState()
        self.createDistrict()
    def createState(self):
    
        dropButton1 = self.ids.dropButton1
    
        dropdown = DropDown(size_hint=(None, None), size=(45 * 8, 75))
        dropdown.bind(on_select=lambda instance, x: setattr(dropButton1, 'text', x))
        for x in range(1):
            btn = Button(text="New York", size_hint_y=None, height=44, background_color = (0.0, 0.447, 0.071, 1))
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
    
        dropButton1.bind(on_press=dropdown.open)
    
      
        globals.state = dropButton1.text

    def createDistrict(self):

        db = globals.client['Contacts']
        collection = db['Info']
    
        dropButton2 = self.ids.dropButton2
    
        dropdown = DropDown(size_hint=(None, None), size=(45 * 8, 75))
    

        options = collection.find({}, {"_id": 0, "District": 1})
    
        for option in options:
            btn = Button(text=option['District'], size_hint_y=None, height=44, background_color = (0.0, 0.447, 0.071, 1))
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            if btn.text != "Not Found":
                dropdown.add_widget(btn)
    
        dropButton2.bind(on_press=dropdown.open)
    
        dropdown.bind(on_select=lambda instance, x: setattr(dropButton2, 'text', x))
        globals.district = dropButton2.text

    def access(self):
        self.createState()
        self.createDistrict()
        self.manager.current = "ViewContact"