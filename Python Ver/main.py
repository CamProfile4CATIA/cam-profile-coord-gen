import kivy

#region Imports


kivy.require("1.9.0")
from kivy.uix.stacklayout import StackLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget


#endregion



class MyCam(object):
    def __init__(self):
        self.rotationSense= None
        self.radius=None
        self.seqArray=None

    def set_rotationSense(self,rot):
        self.rotationSense = rot

    def set_radius(self,rad):
        self.rotationSense = rad

    def set_radius(self,array):
        self.seqArray=array

global Cam
Cam = MyCam()
Cam.set_rotationSense('CW')




class CustomDropDown(BoxLayout):
    pass

class MainWidget(GridLayout):
    pass

#region Screen Classes
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

#endregion

class MainWidgetWrapper(GridLayout):

    def __init__(self,**kwargs):
        super(MainWidgetWrapper,self).__init__(**kwargs)
        self.add_widget(MainWidget(id='mainwid1'))
        self.btn = Button(id='plusbutton1', text='+', height='52dp', size_hint=(0.07, None))
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.addonemore)

    def addonemore(self,instance):
        i = int(instance.id[10:])
        i+=1
        print('The button <%s> is being pressed' % instance.id)
        fillerwidget = Widget(height='52dp', size_hint=(0.07, None))
        self.remove_widget(self.btn)
        self.add_widget(fillerwidget)
        self.add_widget(MainWidget(id='mainwid'+str(i)))
        self.btn.id='plusbutton'+str(i)
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.addonemore)

class CPCGeApp(App):
    def build(self):
        return Builder.load_file("CPCG.kv")


App = CPCGeApp()
App.run()
