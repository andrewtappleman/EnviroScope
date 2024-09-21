from kivy.uix.screenmanager import ScreenManager, Screen
from header_widget import HeaderWidget

class SignUpIn(Screen):
    def __init__(self, **kwargs):
        super(SignUpIn, self).__init__(**kwargs)
        header = HeaderWidget()
        self.add_widget(header)