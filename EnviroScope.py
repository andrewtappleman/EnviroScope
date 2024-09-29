
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
from virtual_badges import VirtualBadges
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
from daily_goals import DailyGoals
from collective_impact import CollectiveImpact
from social_media_page import SocialMediaPage
from litter_sheet import LitterSheet
from pollution_map import PollutionMap
from fun_facts import FunFacts
from post_media import PostMedia
from instruct_post import InstructPost
from out_order import OutOrder
from bottle_count import BottleCount


#Loading Kivy Files
Builder.load_file('FPAY.kv')
Builder.load_file('FunFacts.kv')
Builder.load_file('VirtualBadges.kv')
Builder.load_file('DailyGoals.kv')
Builder.load_file('PostMedia.kv')
Builder.load_file('GetRewarded.kv')
Builder.load_file('GetInspired.kv')
Builder.load_file('GetInContact.kv')
Builder.load_file('CollectiveImpact.kv')
Builder.load_file('LitterSheet.kv')
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
Builder.load_file('AddAJob.kv')
Builder.load_file('ViewJobs.kv')
Builder.load_file('BottleCount.kv')
Builder.load_file('ViewContact.kv')
Builder.load_file('SocialMedia.kv')
Builder.load_file('SocialChat.kv')
Builder.load_file('Parkcount.kv')


width_base = 15
height_base = 25
scale = 30
Window.size = (width_base * scale, height_base * scale)

class MyScreenManager(ScreenManager):
    pass

class EnviroScopeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignUpIn(name = 'SignUpIn'))
        sm.add_widget(OutOrder(name = 'OutOrder'))        
        sm.add_widget(SignIn(name = 'SignIn'))
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
        sm.add_widget(VirtualBadges(name = 'VirtualBadges'))
        sm.add_widget(CollectiveImpact(name = 'CollectiveImpact'))
        sm.add_widget(SocialMediaPage(name = 'SocialMediaPage'))
        sm.add_widget(LitterSheet(name = 'LitterSheet'))
        sm.add_widget(InstructPost(name = 'InstructPost'))
        sm.add_widget(SignUp(name = 'SignUp'))
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
    