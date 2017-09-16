import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

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


class MainLayout(BoxLayout):
    pass


    # Function called when equals is pressed
#    def calculate(self, calculation):
#        if calculation:
#            try:
                # Solve formula and display it in entry
                # which is pointed at by display
#                self.see.text = str(eval(calculation))
#            except Exception:
#                self.see.text = "Error"

class CustomDropDown(BoxLayout):
    pass




class CPCGApp(App):
    def build(self):
        return MainLayout()


App = CPCGApp()
App.run()
