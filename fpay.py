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

class FPAY(Screen):
    link1 = StringProperty("https://mrdoob.com/#/147/google_space")
    link2 = StringProperty("https://mrdoob.com/#/147/google_space")
    link3 = StringProperty("https://mrdoob.com/#/147/google_space")
    link4 = StringProperty("https://mrdoob.com/#/147/google_space")
    link5 = StringProperty("https://mrdoob.com/#/147/google_space")
    def start(self):
        self.api_key = 'AIzaSyB2Q8bhNECnUNFF-ZemwlmSXlSfEzelcWU'
        self.search_engine_id = 'e6b1412f598284e1e'
        notification.notify(title = 'EnviroScope', message = 'Search Pending.')
        self.query = str(self.ids.zipcode.text) + ' environmental issues and conservation and pollution'
        print('query', self.query)
        self.googleSearch()

    def googleSearch(self, **params):
        base_url = 'https://www.googleapis.com/customsearch/v1'
        params.update({
            'key': self.api_key,
            'cx': self.search_engine_id,
            'q': self.query,
            'num': 5
        })
        response = httpx.get(base_url, params=params)
        response.raise_for_status()

        self.finish(response.json())

    def finish(self, response_json):
        search_results = []

        items = response_json.get('items', [])
        for item in items:
            search_results.append(item.get('link'))
        
        df = pd.json_normalize(response_json.get('items', []))

        search_results = df['link'].tolist() if 'link' in df else []
        print(search_results)
        listLen = len(search_results)
        if listLen > 0:
            self.link1 = search_results[0]
        if listLen > 1:
            self.link2 = search_results[1]
        if listLen > 2:
            self.link3 = search_results[2]
        if listLen > 3:
            self.link4 = search_results[3]
        if listLen > 4:
            self.link5 = search_results[4]
        globals.notifLimit += 1
        if globals.notifLimit == 5:
            notification.notify(title = 'EnviroScope', message = 'Search Concluded.')
        
    def perform_search(self):
        self.start()
        for i in range(0, 5, 1):
            self.googleSearch(start=i + 1)
            time.sleep(1)
    
    def makeLink(self):
        webbrowser.open(self.link1)        
        webbrowser.open(self.link2)
        webbrowser.open(self.link3)
        webbrowser.open(self.link4)
        webbrowser.open(self.link5)