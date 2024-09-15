
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

class PostMedia(Screen):

    def NotifyDef(self, instance):
        notification.notify(title = 'EnviroScope', message = 'You have posted your photos.')

        db = globals.client['SocialMedia']
        posts_collection = db['Posts']


        db = globals.client['MainData']
        posts_collection = db['Social Media']


        beforePath = self.ids.beforePhoto.text

        afterPath = self.ids.afterPhoto.text

        caption = self.ids.captionMedia.text


        with open(beforePath, 'rb') as image_file:
            base64_before = base64.b64encode(image_file.read()).decode('utf-8')
        
        with open(afterPath, 'rb') as image_file:
            base64_after = base64.b64encode(image_file.read()).decode('utf-8')

        post = {
            'Name': globals.username,
            'BeforeData': base64_before,
            'AfterData': base64_after,
            'caption': caption
            }

        # Insert the post into MongoDB
        posts_collection.insert_one(post)
        self.manager.current = "GetInvolved"

    def Check(self, instance):
        self.ids.my_image.source = self.ids.beforePhoto.text
        self.ids.my_image2.source = self.ids.afterPhoto.text

        if not os.path.exists(self.ids.my_image.source):
            notification.notify(title = 'EnviroScope', message = 'EnviroScope canot find your before photo.', timeout = 3)
            return None
        
        if not os.path.exists(self.ids.my_image2.source):
            time.sleep(5)
            notification.notify(title = 'EnviroScope', message = 'EnviroScope canot find your after photo.')
            return None