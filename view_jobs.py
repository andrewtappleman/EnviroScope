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

class ViewJobs(Screen):
    Job11 = StringProperty("Default Info")
    Job12 = StringProperty("Default Info")
    Job13 = StringProperty("Default Info")

    Job21 = StringProperty("Default Info")
    Job22 = StringProperty("Default Info")
    Job23 = StringProperty("Default Info")

    Job31 = StringProperty("Default Info")
    Job32 = StringProperty("Default Info")
    Job33 = StringProperty("Default Info")
    
    Job41 = StringProperty("Default Info")
    Job42 = StringProperty("Default Info")
    Job43 = StringProperty("Default Info")
    def on_pre_enter(self):

        db = globals.client['CleanUps']
        collection = db['Jobs']

        db = globals.client['MainData']
        collection = db['Litter Cleanups']

        Job1 = collection.find().sort('_id', -1).skip(3).limit(1)[0]
        self.Job11 = Job1['Location']
        self.Job12 = Job1['Date']
        self.Job13 = Job1['Time']

        Job2 = collection.find().sort('_id', -1).skip(2).limit(1)[0]
        self.Job21 = Job2['Location']
        self.Job22 = Job2['Date']
        self.Job23 = Job2['Time']

        Job3 = collection.find().sort('_id', -1).skip(1).limit(1)[0]
        self.Job31 = Job3['Location']
        self.Job32 = Job3['Date']
        self.Job33 = Job3['Time']

        Job4 = collection.find().sort('_id', -1).limit(1)[0]
        self.Job41 = Job4['Location']
        self.Job42 = Job4['Date']
        self.Job43 = Job4['Time']