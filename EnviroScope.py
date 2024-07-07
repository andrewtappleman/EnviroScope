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
import time


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


width_base = 15
height_base = 25
scale = 30
Window.size = (width_base * scale, height_base * scale)

class NewYorkState(Screen):
    pass
class InspirationalVideos(Screen):
    pass
class VirtualBadges(Screen):
    pass
class SignUpIn(Screen):
    pass
class SignIn(Screen):
    pass
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
    pass 
    
class LitterSheet (Screen):
    nameList = ['Julian Smith', 'Isabella Jones', 'Liam Taylor', 'Ava Martinez', 'Ethan Brown']
    def addToList(self):
        
        appendText = self.ids.litterSign.text
        self.nameList.append(appendText)
        notification.notify(title = 'EnviroScope', message = 'Thank you for signing up.')

class GretaThunberg (Screen):
    pass
class PollutionMap(Screen):
    pass
class FunFacts(Screen):
    pass
class PostMedia(Screen):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            
        except:
            pass

    def selected2(self, filename):
        try:
            self.ids.my_image2.source = filename[0]
            
        except:
            pass

    def NotifyDef(self, instance):
        notification.notify(title = 'EnviroScope', message = 'You have posted your photos.')

class instructPost(Screen):
    pass

class outOrder(Screen):
    pass     

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
        return sm

if __name__ == '__main__':
    EnviroScopeApp().run()