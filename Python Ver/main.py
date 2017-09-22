import kivy

#region Imports

import numpy as np
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
        self.radius = rad

    def set_SeqArray(self,array):
        self.seqArray=array

global Cam
Cam = MyCam()


global SeqArray
SeqArray=np.array([['first', 0, 0, 0],
[0, 0, 0,0]])





class CustomDropDown(BoxLayout):
    pass

class MainWidget(GridLayout):
    def feed(self,row,col,data):
        global SeqArray
        row=int(row)
        col=int(col)
        if row>(SeqArray.size/4):
            newrow=np.array(['first',0, 0, 0])
            SeqArray=np.vstack((SeqArray,newrow))
        SeqArray[(row-1),(col-1)]=data
        print(SeqArray)

    def update_padding(self, text_input, *args):
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached
        )
        text_input.padding_x = (text_input.width - text_width)/2


#region Screen Classes
class PrelimScreen(Screen):
    def assign_rad(self,rad):
        global Cam
        Cam.set_radius(rad)
        print (Cam.radius)



    def assign_rot(self,rot_sens):
        global Cam
        Cam.set_rotationSense(rot_sens)
        print (Cam.rotationSense)

    def update_padding(self, text_input, *args):
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached
        )
        text_input.padding_x = (text_input.width - text_width)/2

class MainScreen(Screen):
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
