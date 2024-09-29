
#:import webbrowser webbrowser

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
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

class DailyGoals (Screen):
    Goal1 = StringProperty('Default Goal')
    Goal2 = StringProperty('Default Goal')
    Goal3 = StringProperty('Default Goal')
    Goal4 = StringProperty('Default Goal')
    Goal5 = StringProperty('Default Goal')
    def on_pre_enter(self):
        if globals.new == 0:
            self.regen()
            globals.new = 1

    def regen(self):
        print("Unique")
        goalNum1 = random.randint(0, 19)

        goalNum2 = random.randint(0, 19)
        while goalNum2 == goalNum1:
            goalNum2 = random.randint(0, 19)

        goalNum3 = random.randint(0, 19)
        while goalNum3 == goalNum2 or goalNum3 == goalNum1:
            goalNum3 = random.randint(0, 19)

        goalNum4 = random.randint(0, 19)
        while goalNum4 == goalNum3 or goalNum4 == goalNum2 or goalNum4 == goalNum1:
            goalNum4 = random.randint(0, 19)

        goalNum5 = random.randint(0, 19)
        while goalNum5 == goalNum4 or goalNum5 == goalNum3 or goalNum5 == goalNum2 or goalNum5 == goalNum1:
            goalNum3 = random.randint(0, 19)
        
        db = globals.client['MainData']
        collection = db['Daily Goals']
        
        num1 = goalNum1
        num2 = goalNum2
        num3 = goalNum3
        num4 = goalNum4
        num5 = goalNum5
        
        findDoc = collection.find().sort({'_id': -1}).skip(num1).limit(1)[0]
        self.Goal1 = findDoc['Goal']

        findDoc = collection.find().sort({'_id': -1}).skip(num2).limit(1)[0]
        self.Goal2 = findDoc['Goal']

        findDoc = collection.find().sort({'_id': -1}).skip(num3).limit(1)[0]
        self.Goal3 = findDoc['Goal']

        findDoc = collection.find().sort({'_id': -1}).skip(num4).limit(1)[0]
        self.Goal4 = findDoc['Goal']

        findDoc = collection.find().sort({'_id': -1}).skip(num5).limit(1)[0]
        self.Goal5 = findDoc['Goal']