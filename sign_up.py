import globals

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
Builder.load_file("SignUp.kv")


class SignUp(Screen):

    def addInfo(self):
        if self.ids.UserName2.text == 'User Name':
            notification.notify(title = 'EnviroScope', message = 'That username is reserved for admin.')
        else:
            db = globals.client["MainData"]
            my_collection = db["Account Info"]
            globals.new2 = 1
            
            NameData = [{"name": self.ids.UserName2.text, "password": self.ids.Password2.text, "Bottles": 0, "Parks": 0, "streak": 1, "last_date": datetime.now(), 'GoalFind1': 1, 'GoalFind2': 1, 'GoalFind3': 1, 'GoalFind4': 1, 'GoalFind5': 1, }]
            globals.username = self.ids.UserName2.text
            print(NameData)
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

