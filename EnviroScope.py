
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


#Loading Python Files
from park_count import ParkCount
from social_media import SocialMedia
from social_chat import SocialChat
from view_contact import ViewContact
from new_york_state import NewYorkState
from inspirational_videos import InspirationalVideos
from virtual_badges import VirtualBadges
from video1 import Video1
from sign_up_in import SignUpIn
from sign_in import SignIn
from sign_up import SignUp
from fpay import FPAY
from add_a_job import AddAJob
from environmental_issues import EnvironmentalIssues
from get_in_contact import GetInContact
from view_jobs import ViewJobs
from get_informed import GetInformed
from get_rewarded import GetRewarded
from get_involved import GetInvolved
from get_inspired import GetInspired
from leaderboard import LeaderBoard
from daily_streaks import DailyStreaks
from daily_goals import DailyGoals
from collective_impact import CollectiveImpact
from famous_advocates import FamousAdvocates
from social_media_page import SocialMediaPage
from litter_sheet import LitterSheet
from greta_thunberg import GretaThunberg
from pollution_map import PollutionMap
from fun_facts import FunFacts
from post_media import PostMedia
from instruct_post import InstructPost
from out_order import OutOrder
from bottle_count import BottleCount


#Loading Kivy Files
Builder.load_file('FPAY.kv')
Builder.load_file('PollutionMap.kv')
Builder.load_file('FunFacts.kv')
Builder.load_file('NewYorkState.kv')
Builder.load_file('VirtualBadges.kv')
Builder.load_file('DailyGoals.kv')
Builder.load_file('PostMedia.kv')
Builder.load_file('GetRewarded.kv')
Builder.load_file('GetInspired.kv')
Builder.load_file('GretaThunberg.kv')
Builder.load_file('GetInContact.kv')
Builder.load_file('CollectiveImpact.kv')
Builder.load_file('LitterSheet.kv')
Builder.load_file('InspirationalVideos.kv')
Builder.load_file('DailyStreaks.kv')
Builder.load_file('SocialMediaPage.kv')
Builder.load_file('InstructPost.kv')
Builder.load_file('LeaderBoard.kv')
Builder.load_file('SignUpIn.kv')
Builder.load_file('SignIn.kv')
Builder.load_file('EnvironmentalIssues.kv')
Builder.load_file('GetInvolved.kv')
Builder.load_file('outOrder.kv')
Builder.load_file('GetInformed.kv')
Builder.load_file('SignUp.kv')
Builder.load_file('Video1.kv')
Builder.load_file('AddAJob.kv')
Builder.load_file('ViewJobs.kv')
Builder.load_file('BottleCount.kv')
Builder.load_file('ViewContact.kv')
Builder.load_file('SocialMedia.kv')
Builder.load_file('SocialChat.kv')



uri = "mongodb+srv://admin:admin@enviroscopecluster0.qdwjcoq.mongodb.net/?appName=EnviroScopeCluster0"
# Create a new client and connect to the server
clientel = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    clientel.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
globals.client = clientel

width_base = 15
height_base = 25
scale = 30
Window.size = (width_base * scale, height_base * scale)

class MyScreenManager(ScreenManager):
    pass
<<<<<<< HEAD
class SocialChat(Screen):
    Entry1 = StringProperty('Default Text')
    Entry2 = StringProperty('Default Text')
    Entry3 = StringProperty('Default Text')
    Entry4 = StringProperty('Default Text')
    Entry5 = StringProperty('Default Text')

    Name1 = StringProperty('Default Text')
    Name2 = StringProperty('Default Text')
    Name3 = StringProperty('Default Text')
    Name4 = StringProperty('Default Text')
    Name5 = StringProperty('Default Text')

    def on_enter(self):
        self.refresh()
    def refresh(self):
        global client
        global username
        db = client['MainData']
        collection = db['Chat']
        EntryFind1 = collection.find().sort('_id', -1).skip(4).limit(1)[0]
        EntryFind2 = collection.find().sort('_id', -1).skip(3).limit(1)[0]
        EntryFind3 = collection.find().sort('_id', -1).skip(2).limit(1)[0]
        EntryFind4 = collection.find().sort('_id', -1).skip(1).limit(1)[0]
        EntryFind5 = collection.find().sort('_id', -1).limit(1)[0]

        self.Entry1 = EntryFind1['Entry']
        self.Name1 = EntryFind1['Username']
        self.Entry2 = EntryFind2['Entry']
        self.Name2 = EntryFind2['Username']
        self.Entry3 = EntryFind3['Entry']
        self.Name3 = EntryFind3['Username']
        self.Entry4 = EntryFind4['Entry']
        self.Name4 = EntryFind4['Username']
        self.Entry5 = EntryFind5['Entry']
        self.Name5 = EntryFind5['Username']
    
    def addToDB(self):
        global client
        global username
        db = client['MainData']
        collection = db['Chat']
        FullEntry = self.ids.EntryInput.text

        query = [{"Username": username, "Entry": FullEntry}]
        
        try:
            result = collection.insert_many(query)
        except pymongo.errors.OperationFailure:
            print("An authentication error was received. Check your database user permissions.")
            print('')
            print('')
            sys.exit(1)
        else:
            inserted_count = len(result.inserted_ids)
            print("I inserted %d documents." % inserted_count)
            print("")
            print('')
        self.refresh()


class viewContact(Screen):
    Phone1 = StringProperty("Default Info")
    Address1 = StringProperty("Default Info")
    Role1 = StringProperty("Default Info")

    Phone2 = StringProperty("Default Info")
    Address2 = StringProperty("Default Info")
    Role2 = StringProperty("Default Info")

    Phone3 = StringProperty("Default Info")
    Address3 = StringProperty("Default Info")
    Role3 = StringProperty("Default Info")
    
    def on_pre_enter(self):
        global state
        global district
        global clientDaily
        db = client['Contacts']
        collection = db['Info']
        
        cursor = collection.find({"State": state}).limit(2)
    
        stateInfo = list(cursor)
        print(stateInfo)
        print("Querying for state:", state)
        print("State Info Results:", stateInfo)
    
        Person1 = stateInfo[0]
        self.Role1 = Person1['Role']
        self.Address1 = Person1['Address']
        self.Phone1 = Person1['Phone']

        Person2 = stateInfo[1]
        self.Role2 = Person2['Role']
        self.Address2 = Person2['Address']
        self.Phone2 = Person2['Phone']



        cursor = collection.find({"District": district}).limit(1)
        districtInfo = list(cursor)
        Person3 = districtInfo[0]
        self.Role3 = Person3['Role']
        self.Address3 = Person3['Address']
        self.Phone3 = Person3['Phone']


class NewYorkState(Screen):
    pass
class InspirationalVideos(Screen):
    pass
class VirtualBadges(Screen):
    pass
class Video1(Screen):
    pass

class SignUpIn(Screen):
    pass
class AddAJob(Screen):
    def on_enter(self):
        global username
        self.ids.NameInput.text = username
    

    def addToList(self):  


        notification.notify(title = 'EnviroScope', message = 'You have created a clean up.')      
        global client
        db = client['CleanUps']
        collection = db['Jobs']
        db = client['MainData']
        collection = db['Litter Cleanups']
        
        name = self.ids.NameInput.text
        location = self.ids.Location.text
        date = self.ids.Date.text
        time = self.ids.Time.text
        
        query = [{"Name": name, "Location": location, "Date": date, "Time": time}]
        
        try:
            result = collection.insert_many(query)
        except pymongo.errors.OperationFailure:
            print("An authentication error was received. Check your database user permissions.")
            sys.exit(1)
        else:
            inserted_count = len(result.inserted_ids)
            print("I inserted %d documents." % inserted_count)
            print("\n")

class SignIn(Screen):
    
    def check_account(self):
        
        global username
        global client
        db = client['AccountInfo']
        collection = db['NamePassword']
        global new
        global username

        new = 0

        db = client['MainData']
        collection = db['Account Info']
        
        user_name = self.ids.UserName1.text

        username = self.ids.UserName1.text

        password = self.ids.Password1.text
        
        query = {"name": user_name, "password": password}
        
        if self.check_for_type(collection, query):
            self.manager.current = "EnvironmentalIssues"
        else:
            notification.notify(title = 'EnviroScope', message = 'No account found.')
            self.ids.UserName1.text = ""
            self.ids.Password1.text = ""


    def check_for_type(self, collection, query):
        result = collection.find_one(query)
        return result is not None


class SignUp(Screen):
    
    def addInfo(self):
        global new
        global client
        db = client["AccountInfo"]
        my_collection = db["NamePassword"]

        NameData = [{"name": self.ids.UserName2.text, "password": self.ids.Password2.text}]
        new = 1
        username = self.ids.UserName2.text

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
        
class EnvironmentalIssues (Screen):
    pass
   
class GetInContact (Screen):
    pass

    link1 = StringProperty("https://mrdoob.com/#/147/google_space")
    link2 = StringProperty("https://mrdoob.com/#/147/google_space")
    link3 = StringProperty("https://mrdoob.com/#/147/google_space")
    link4 = StringProperty("https://mrdoob.com/#/147/google_space")
    link5 = StringProperty("https://mrdoob.com/#/147/google_space")
    def start(self):
        self.api_key = 'AIzaSyB2Q8bhNECnUNFF-ZemwlmSXlSfEzelcWU'
        self.search_engine_id = 'e6b1412f598284e1e'
        notification.notify(title = 'EnviroScope', message = 'Search Pending.')
        self.query = str(self.ids.zipcode.text)
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
        global notifLimit
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
        notifLimit += 1
        if notifLimit == 5:
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


class EnvironmentalIssues (Screen):
    pass
        
   
class GetInContact (Screen):
    def on_pre_enter(self):
        self.createState()
        self.createDistrict()
    def createState(self):
        global client
        global state
    
        dropButton1 = self.ids.dropButton1
    
        dropdown = DropDown(size_hint=(None, None), size=(45 * 8, 75))
        dropdown.bind(on_select=lambda instance, x: setattr(dropButton1, 'text', x))
        for x in range(1):
            btn = Button(text="New York", size_hint_y=None, height=44, background_color = (0.0, 0.447, 0.071, 1))
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
    
        dropButton1.bind(on_press=dropdown.open)
    
      
        state = dropButton1.text

    def createDistrict(self):
        global client
        global district
        db = client['Contacts']
        collection = db['Info']
    
        dropButton2 = self.ids.dropButton2
    
        dropdown = DropDown(size_hint=(None, None), size=(45 * 8, 75))
    

        options = collection.find({}, {"_id": 0, "District": 1})
    
        for option in options:
            btn = Button(text=option['District'], size_hint_y=None, height=44, background_color = (0.0, 0.447, 0.071, 1))
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            if btn.text != "Not Found":
                dropdown.add_widget(btn)
    
        dropButton2.bind(on_press=dropdown.open)
    
        dropdown.bind(on_select=lambda instance, x: setattr(dropButton2, 'text', x))
        district = dropButton2.text

    def access(self):
        self.createState()
        self.createDistrict()
        self.manager.current = "viewContact"
        
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

        global client
        db = client['CleanUps']
        collection = db['Jobs']

        db = client['MainData']
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

 
class GetInformed (Screen):
    
    pass
class GetRewarded (Screen):
    pass
    
class GetInvolved (Screen):
    pass

class GetInspired (Screen):
    pass

class LeaderBoard (Screen):
    pass 
    
class DailyStreaks (Screen):
    pass

class DailyGoals (Screen):
    pass 
     
class CollectiveImpact (Screen):

     
     def addInfo(self):

        global client
        db = client["BottleCountInfo"]
        
        my_collection = db["TotalBottles"]
        NameData = [{"Bottles": self.ids.TotalBottles2.text}]

        global Bottles
        Bottles = self.id.TotalBottles2.text

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
     


class DailyGoals (Screen):
    pass 

class CollectiveImpact (Screen):
    pass 

class FamousAdvocates (Screen):
    pass

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

        global client
        db = client['SocialMedia']
        collection = db['Posts']


        db = client['MainData']
        collection = db['Social Media']

        global username

        

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
    
    
class LitterSheet (Screen):
    def on_enter(self):
        global username
        self.ids.NameInput.text = username
        self.create_dropdown()

    def create_dropdown(self):
        global client
        db = client['CleanUps']
        collection = db['Jobs']

        db = client['MainData']
        collection = db['Litter Cleanups']

        dropButton = self.ids.dropButton
    
        dropdown = DropDown(size_hint=(None, None), size=(45 * 8, 75))
    

        options = collection.find({}, {"_id": 0, "Location": 1})
    
        for option in options:
            btn = Button(text=option['Location'], size_hint_y=None, height=44)

            btn = Button(text=option['Location'], size_hint_y=None, height=44, background_color = (0.4196, 0.7922, 0.9569, 1))

            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
    
        dropButton.bind(on_press=dropdown.open)
    
        dropdown.bind(on_select=lambda instance, x: setattr(dropButton, 'text', x))

    def addToList(self):
        
        notification.notify(title = 'EnviroScope', message = 'You have joined a clean up.')
        global username
        global client
        db = client['LitterSheet']
        collection = db['Jobs']


        db = client['MainData']
        collection = db['Litter Cleanups']
        
        name = self.ids.NameInput.text
        cleanup = self.ids.dropButton.text
        
        query = [{"Name": name, "Location": cleanup}]
        
        try:
            result = collection.insert_many(query)
        except pymongo.errors.OperationFailure:
            print("An authentication error was received. Check your database user permissions.")
            sys.exit(1)
        else:
            inserted_count = len(result.inserted_ids)
            print("I inserted %d documents." % inserted_count)
            print("\n")

class GretaThunberg (Screen):
    pass
class PollutionMap(Screen):
    pass
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
        
        global client

        db = client['FunFacts']
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
    
class PostMedia(Screen):

    def NotifyDef(self, instance):
        notification.notify(title = 'EnviroScope', message = 'You have posted your photos.')

        global client
        db = client['SocialMedia']
        posts_collection = db['Posts']


        db = client['MainData']
        posts_collection = db['Social Media']


        beforePath = self.ids.beforePhoto.text

        afterPath = self.ids.afterPhoto.text

        caption = self.ids.captionMedia.text


        with open(beforePath, 'rb') as image_file:
            base64_before = base64.b64encode(image_file.read()).decode('utf-8')
        
        with open(afterPath, 'rb') as image_file:
            base64_after = base64.b64encode(image_file.read()).decode('utf-8')

        global username
        post = {
            'Name': username,
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

class instructPost(Screen):
    pass

class outOrder(Screen):
    pass     

class BottleCount (Screen):

    def check_account(self):
        
        global Bottles
        global client
        db = client['BottleCountInfo']
        collection = db['TotalBottles']
        
        Total_Bottles = self.ids.TotalBottles1.text

        Bottles = self.ids.TotalBottle1.text
        
        query = {"Bottles": Total_Bottles}
        
        if self.check_for_type(collection, query):
            self.manager.current = "EnvironmentalIssues"
        else:
            notification.notify(title = 'EnviroScope', message = 'Bottle count was not sucseful in updating')
            self.ids.TotalBottles1.text = ""


    def check_for_type(self, collection, query):
        result = collection.find_one(query)
        return result is not None



    TotalBottles = StringProperty("5")
    def addInfo(self):

        global client
        db = client["CollectiveImpact"]
        
        my_collection = db["TotalBottles"]
        data = self.ids.EnterHere2.text
        NameData = [{"Bottles": data}]

        global Bottles
        self.Bottles = self.ids.EnterHere2.text

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
    def getInfo(self):
        global client
        db = client["CollectiveImpact"]
        
        my_collection = db["TotalBottles"]
        self.TotalBottles = -1
        #Purpose is to get the numebr of bottles
        x = 0
        while self.TotalBottles == -1:
            if my_collection.find({'Bottles': str(x)}) == True:
                self.TotalBottles = my_collection.find({'Bottles': str(x)})
class ParkCount(Screen):
    TotalParks = StringProperty("5")
    def addInfo(self):

        global client
        db = client["CollectiveImpact"]
        
        my_collection = db["TotalBottles"]
        data = self.ids.Submit2.text
        NameData = [{"Bottles": data}]

        global Parks
        self.Parks = self.ids.Submit2.text

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
    def getInfo(self):
        global client
        db = client["CollectiveImpact"]
        
        my_collection = db["TotalParks"]
        self.TotalParks = -1
        #Purpose is to get the numebr of bottles
        x = 0
        while self.TotalParks == -1:
            if my_collection.find({'Parks': str(x)}) == True:
                self.TotalParkss = my_collection.find({'Parks': str(x)})
=======
>>>>>>> 89d539953b5aaad6006ae5b6c9d759febd6ab323

class EnviroScopeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignUpIn(name = 'SignUpIn'))
        sm.add_widget(OutOrder(name = 'OutOrder'))        
        sm.add_widget(SignIn(name = 'SignIn'))
        sm.add_widget(NewYorkState(name = 'NewYorkState'))
        sm.add_widget(GetInformed(name = 'GetInformed'))
        sm.add_widget(FPAY(name = 'FPAY')) 
        sm.add_widget(PollutionMap(name = 'PollutionMap'))
        sm.add_widget(FunFacts(name = 'FunFacts'))
        sm.add_widget(PostMedia(name = 'PostMedia'))
        sm.add_widget(EnvironmentalIssues(name = 'EnvironmentalIssues'))
        sm.add_widget(GetInvolved(name = 'GetInvolved'))
        sm.add_widget(GetInContact(name = 'GetInContact'))
        sm.add_widget(GetRewarded(name = 'GetRewarded'))
        sm.add_widget(GetInspired(name = 'GetInspired'))
        sm.add_widget(LeaderBoard(name = 'LeaderBoard'))
        sm.add_widget(DailyGoals(name = 'DailyGoals'))
        sm.add_widget(DailyStreaks(name = 'DailyStreaks'))
        sm.add_widget(VirtualBadges(name = 'VirtualBadges'))
        sm.add_widget(CollectiveImpact(name = 'CollectiveImpact'))
        sm.add_widget(FamousAdvocates(name = 'FamousAdvocates'))
        sm.add_widget(SocialMediaPage(name = 'SocialMediaPage'))
        sm.add_widget(LitterSheet(name = 'LitterSheet'))
        sm.add_widget(GretaThunberg(name = 'GretaThunberg'))
        sm.add_widget(InstructPost(name = 'InstructPost'))
        sm.add_widget(SignUp(name = 'SignUp'))
        sm.add_widget(InspirationalVideos(name = 'InspirationalVideos'))
        sm.add_widget(Video1(name = 'Video1'))
        sm.add_widget(AddAJob(name = 'AddAJob'))
        sm.add_widget(ViewJobs(name = 'ViewJobs'))
        sm.add_widget(BottleCount(name = 'BottleCount'))
        sm.add_widget(ParkCount(name = 'ParkCount'))
        sm.add_widget(ViewContact(name = 'ViewContact'))
        sm.add_widget(SocialMedia(name = 'SocialMedia'))
        sm.add_widget(SocialChat(name = 'SocialChat'))
        return sm

if __name__ == '__main__':
    EnviroScopeApp().run()