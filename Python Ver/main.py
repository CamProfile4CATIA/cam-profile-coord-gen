import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang.builder import Builder

#Classes

class PrelimScreen(Screen):
#Ask for rotatin  sense and radius
    pass

class MainScreen(Screen):
#Ask for motions and other parameters
    pass

class PostScreen(Screen):
#Ask for Output file location
    pass

class FinalScreen(Screen):
#Progress bar, furteher how to, credits profile plot
    pass

class ScrMgt(ScreenManager):
    pass

class CustomDropDown(BoxLayout):
    pass

class CustomDropDown1(BoxLayout):
    pass

MasterLayout = Builder.load_file("CPCG.kv")

class CPCGApp(App):
    def build(self):
        return MasterLayout


App = CPCGApp()
App.run()
