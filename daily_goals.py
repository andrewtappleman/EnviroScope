
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

    def loadPrev(self):
        db = globals.client['MainData']
        collection = db['Account Info']
        
        findDoc = collection.find({'name': globals.username}).limit(1)[0]

        num1 = str(findDoc['GoalFind1'])
        num2 = str(findDoc['GoalFind2'])
        num3 = str(findDoc['GoalFind3'])
        num4 = str(findDoc['GoalFind4'])
        num5 = str(findDoc['GoalFind5'])

        print(num1, num2, num3, num4, num5)
        print('Numbers')

        db = globals.client['MainData']
        collection = db['Daily Goals']

        findDoc = collection.find_one({'FindNum': num1})
        self.Goal1 = findDoc['Goal']

        findDoc = collection.find_one({'FindNum': num2})
        self.Goal2 = findDoc['Goal']

        findDoc = collection.find_one({'FindNum': num3})
        self.Goal3 = findDoc['Goal']

        findDoc = collection.find_one({'FindNum': num4})
        self.Goal4 = findDoc['Goal']

        findDoc = collection.find_one({'FindNum': num5})
        self.Goal5 = findDoc['Goal']

    def regen(self):
        print("Unique")
        
        goal_numbers = random.sample(range(1, 20), 5)

        goalNum1, goalNum2, goalNum3, goalNum4, goalNum5 = goal_numbers
        print('Got Numbers')
        

        db = globals.client['MainData']
        collection = db['Daily Goals']
        
        num1 = str(goalNum1)
        num2 = str(goalNum2)
        num3 = str(goalNum3)
        num4 = str(goalNum4)
        num5 = str(goalNum5)
        print(num1, num2, num3, num4, num5)
        print('Numbers')


        findDoc = collection.find_one({'FindNum': num1})
        self.Goal1 = findDoc['Goal']

        findDoc = collection.find_one({'FindNum': num2})
        self.Goal2 = findDoc['Goal']

        findDoc = collection.find_one({'FindNum': num3})
        self.Goal3 = findDoc['Goal']

        findDoc = collection.find_one({'FindNum': num4})
        self.Goal4 = findDoc['Goal']

        findDoc = collection.find_one({'FindNum': num5})
        self.Goal5 = findDoc['Goal']

        db = globals.client['MainData']
        collection = db['Account Info']

        query_filter = {'name': globals.username}
        update_values = {'$set': {'GoalFind1': num1, 'GoalFind2': num2, 'GoalFind3': num3, 'GoalFind4': num4, 'GoalFind5': num5}}

        result = collection.update_one(query_filter, update_values)

    def on_pre_enter(self):
        try:
            if globals.goalCheck == 0:
                globals.goalCheck = 1
                self.regen()
            elif globals.new == 1:
                print('Evaluation if new regen')
                self.regen()
            elif globals.new == 0:
                print('Evaluation elif new loadPrev')
                self.loadPrev()
        except Exception as e:
            print(f"Error in on_pre_enter: {e}")
