
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

class SocialMediaPage (Screen):
    
    textureAfter1 = ObjectProperty(None)
    textureBefore1 = ObjectProperty(None)
    textureAfter2 = ObjectProperty(None)
    textureBefore2 = ObjectProperty(None)
    textureAfter3 = ObjectProperty(None)
    textureBefore3 = ObjectProperty(None)

    caption1 = StringProperty("Default Caption")
    caption2 = StringProperty("Default Caption")
    caption3 = StringProperty("Default Caption")
    name1 = StringProperty("Default Name")
    name2 = StringProperty("Default Name")
    name3 = StringProperty("Default Name")

    def on_enter(self, *args):
        self.Social()
    def Social(self):

        db = globals.client['SocialMedia']
        collection = db['Posts']


        db = globals.client['MainData']
        collection = db['Social Media']

        PhotoID1 = collection.find().sort('_id', -1).skip(2).limit(1)[0]
        self.name1 = PhotoID1["Name"]
    
        imageBefore1 = PhotoID1['BeforeData']
        image_Before1 = base64.b64decode(imageBefore1)
        imageAfter1 = PhotoID1['AfterData']
        image_After1 = base64.b64decode(imageAfter1)
        self.caption1 = PhotoID1['caption']
    
        dataBefore1 = BytesIO(image_Before1)
        dataAfter1 = BytesIO(image_After1)

        coreBefore1 = CoreImage(dataBefore1, ext='png')
        coreAfter1 = CoreImage(dataAfter1, ext='png')

        self.textureBefore1 = coreBefore1.texture
        self.textureAfter1 = coreAfter1.texture

    
        PhotoID2 = collection.find().sort('_id', -1).skip(1).limit(1)[0]
        self.name2 = PhotoID2["Name"]

        imageBefore2 = PhotoID2['BeforeData']
        image_Before2 = base64.b64decode(imageBefore2)
        imageAfter2 = PhotoID2['AfterData']
        image_After2 = base64.b64decode(imageAfter2)
        self.caption2 = PhotoID2['caption']
    
        dataBefore2 = BytesIO(image_Before2)
        dataAfter2 = BytesIO(image_After2)

        coreBefore2 = CoreImage(dataBefore2, ext='png')
        coreAfter2 = CoreImage(dataAfter2, ext='png')

        self.textureBefore2 = coreBefore2.texture
        self.textureAfter2 = coreAfter2.texture
    
    
        PhotoID3 = collection.find().sort('_id', -1).limit(1)[0]
        self.name3 = PhotoID3["Name"]

        imageBefore3 = PhotoID3['BeforeData']
        image_Before3 = base64.b64decode(imageBefore3)
        imageAfter3 = PhotoID3['AfterData']
        image_After3 = base64.b64decode(imageAfter3)
        self.caption3 = PhotoID3['caption']
    
        dataBefore3 = BytesIO(image_Before3)
        dataAfter3 = BytesIO(image_After3)

        coreBefore3 = CoreImage(dataBefore3, ext='png')
        coreAfter3 = CoreImage(dataAfter3, ext='png')

        self.textureBefore3 = coreBefore3.texture
        self.textureAfter3 = coreAfter3.texture