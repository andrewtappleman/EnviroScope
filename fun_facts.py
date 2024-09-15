
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

class FunFacts(Screen):
    def regen(self):
        factNum1 = random.randint(1, 50)

        factNum2 = random.randint(1, 50)
        while factNum2 == factNum1:
            factNum2 = random.randint(1, 50)

        factNum3 = random.randint(1, 50)
        while factNum3 == factNum2 or factNum3 == factNum1:
            factNum3 = random.randint(1, 50)

        factNum4 = random.randint(1, 50)
        while factNum4 == factNum3 or factNum4 == factNum2 or factNum4 == factNum1:
            factNum4 = random.randint(1, 50)

        factNum5 = random.randint(1, 50)
        while factNum5 == factNum4 or factNum5 == factNum3 or factNum5 == factNum2 or factNum5 == factNum1:
            factNum3 = random.randint(1, 50)
        
        db = globals.client['FunFacts']
        collection = db['Facts']
        
        num1 = str(factNum1)
        num2 = str(factNum2)
        num3 = str(factNum3)
        num4 = str(factNum4)
        num5 = str(factNum5)
        
        print(num1, "\n", num2, "\n", num3, "\n", num4, "\n", num5)
        result = collection.find_one({"Number": num1})
        if result is None:
            print("No results found.")
            return
        fact = result["Fact"]
        self.ids.Fact1.text = fact


        result = collection.find_one({"Number": num2})
        if result is None:
            print("No results found.")
            return
        fact = result["Fact"]
        self.ids.Fact2.text = fact


        result = collection.find_one({"Number": num3})
        if result is None:
            print("No results found.")
            return
        fact = result["Fact"]
        self.ids.Fact3.text = fact


        result = collection.find_one({"Number": num4})
        if result is None:
            print("No results found.")
            return
        fact = result["Fact"]
        self.ids.Fact4.text = fact


        result = collection.find_one({"Number": num5})
        if result is None:
            print("No results found.")
            return
        fact = result["Fact"]
        self.ids.Fact5.text = fact