
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

class EnvironmentalIssues(Screen):
    def on_pre_enter(self):
        self.updateStreak()
    def updateStreak(self):
        today = datetime.now()
        db = globals.client['MainData']
        collection = db['Account Info']
        streakDoc = collection.find_one({'name': globals.username})
        print(globals.username)

        if streakDoc:
            self.last_active_date = streakDoc['last_date']
            streak = streakDoc['streak']
            print("streak streak declaration ", streak)
                       
            if self.last_active_date.date() == (today - timedelta(days=1)).date():
                streak += 1
                print("streak streak evaluation if ", streak)

            elif self.last_active_date.date() == today.date():
                streak = streak
                print("streak streak evaluation elif ", streak)

            else:
                streak = 1
                print("streak streak evaluation else ", streak)


            notification.notify(title='EnviroScope', message=f'Your streak is {streak}.')

            query_filter = {'name': globals.username}
            update_values = {'$set': {'streak': streak, 'last_date': today}}

            result = collection.update_one(query_filter, update_values)
            print(f'Documents updated: {result.modified_count}')
