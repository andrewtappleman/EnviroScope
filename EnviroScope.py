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
import pymongo
import sys
import base64
from pymongo.server_api import ServerApi
import random


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
Builder.load_file('instructPost.kv')
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

uri = "mongodb+srv://admin:admin@enviroscopecluster0.qdwjcoq.mongodb.net/?appName=EnviroScopeCluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

width_base = 15
height_base = 25
scale = 30
Window.size = (width_base * scale, height_base * scale)

username = ''

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

        global client
        db = client["AccountInfo"]
        
        my_collection = db["NamePassword"]
        NameData = [{"name": self.ids.UserName2.text, "password": self.ids.Password2.text}]

        global username
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
    
        dropButton = self.ids.dropButton
    
        dropdown = DropDown(size_hint=(None, None), size=(45 * 8, 75))
    

        options = collection.find({}, {"_id": 0, "Location": 1})
    
        for option in options:
            btn = Button(text=option['Location'], size_hint_y=None, height=44)
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
class EnviroScopeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignUpIn(name = 'SignUpIn'))
        sm.add_widget(outOrder(name = 'outOrder'))        
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
        sm.add_widget(instructPost(name = 'instructPost'))
        sm.add_widget(SignUp(name = 'SignUp'))
        sm.add_widget(InspirationalVideos(name = 'InspirationalVideos'))
        sm.add_widget(Video1(name = 'Video1'))
        sm.add_widget(AddAJob(name = 'AddAJob'))
        sm.add_widget(ViewJobs(name = 'ViewJobs'))
        sm.add_widget(BottleCount(name = 'BottleCount'))
        sm.add_widget(ParkCount(name = 'ParkCount'))
        return sm

if __name__ == '__main__':
    EnviroScopeApp().run()