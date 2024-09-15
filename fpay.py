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
    
    def GiveInfo(self):
        
        Info14901 = 'The Elmira School District bought abandoned land with a past of\nindustrialization.  At only a buck, this was no miracle deal. The site was\npolluted for more than a century.  In Room 127, therewas a test\nthat showed traces of TCE gases seeping into the school.'
        
        Info13760 = 'There is hazardous waste where the IBM factories\nwhere BAE Systems is now stationed.  The estimated cost\nfor cleaning up all waste is guessed at about 10 Million.\nThere are still toxic chemicals beneath the buildings but\nDEC staff said these are the most difficult pockets to clean.'
        if self.ids.ZipcodeInfo.text == '13760':
            self.ids.InfoLabel.text = Info13760
            
        elif self.ids.ZipcodeInfo.text == '14901':
            self.ids.InfoLabel.text = Info14901
            
        elif self.ids.ZipcodeInfo.text == '14904':
            self.ids.InfoLabel.text = Info14901
            
        elif self.ids.ZipcodeInfo.text == '14905':
            self.ids.InfoLabel.text = Info14901
        
        else:
            self.ids.InfoLabel.text = 'Sorry, this is only a prototype.  This zipcode has\nnot been added to the database. Thank you.'
    