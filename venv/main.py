import os
import threading
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


class MainScreen(Widget):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class MainApp(App):
    def build(self):
        self.terminate = 0
        ############################# attaching the main screen #########################
        self.screen_manager = ScreenManager()
        self.first = MainScreen()
        screen1 = Screen(name='mainscreen')
        screen1.add_widget(self.first)
        self.screen_manager.add_widget(screen1)
        return self.screen_manager


MainApp().run()
