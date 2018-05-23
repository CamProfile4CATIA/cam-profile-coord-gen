import kivy

#region Imports

from MyCam import MyCam
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
from kivy.uix.popup import Popup
import xlsxwriter
from kivy.uix.progressbar import ProgressBar
import os
import tkinter as tk
from tkinter import filedialog


#endregion


application_window = tk.Tk()
application_window.withdraw()



global Cam
Cam = MyCam()
Cam.op_file_format='txt'
Cam.path='cord.txt'

global SeqArray
SeqArray=np.array([['Dwell', 'SHM', 0, 0],
['Dwell', 'SHM', 0, 0]])

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
#        print(SeqArray)

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
#        print (Cam.radius)

    def assign_rot(self,rot_sens):
        global Cam
        Cam.set_rotationSense(rot_sens)
#        print (Cam.rotationSense)

    def update_padding(self, text_input, *args):
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached
        )
        text_input.padding_x = (text_input.width - text_width)/2

class MainScreen(Screen):
    def assign_SeqArray(self):
        global Cam
        global SeqArray
        Cam.set_SeqArray(SeqArray)
#        print (Cam.seqArray)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class PostScreen(Screen):
    def generate_cord(self, *args):
        global Cam
        Cam.master_executor()
        if Cam.op_file_format == 'txt':
            with open(os.path.join(Cam.path), 'w') as stream:
                npoints = len(Cam.x)

                for i in range(npoints):
                    xpoint=str(Cam.x[i])
                    ypoint=str(Cam.y[i])
                    stream.write(xpoint)
                    stream.write(' ')
                    stream.write(ypoint)
                    stream.write('\n')

        if Cam.op_file_format == 'xlsx':
            workbook = xlsxwriter.Workbook(Cam.path)
            worksheet = workbook.add_worksheet("coordinates")
            npoints = len(Cam.x)

            for i in range(npoints):
                xpoint = float(Cam.x[i])
                ypoint = float(Cam.y[i])
                col=0
                worksheet.write(i, 0, xpoint)
                worksheet.write(i, 1, ypoint)


    def show_save(self):
        options = {}
        global Cam
        if Cam.op_file_format=='txt':
            options['defaultextension'] = 'txt'
            options['filetypes'] = [('text files', '.txt')]
        if Cam.op_file_format=='xlsx':
            options['defaultextension'] = 'xlsx'
            options['filetypes'] = [('excel files', '.xlsx')]

        options['initialdir'] = None
        options['initialfile'] = None
        options['title'] = None
        Cam.path= str(filedialog.asksaveasfilename(**options))



    def checkbox_txt_selected(self,instance,value):
        if value is True:
            global Cam
            Cam.op_file_format='txt'
#            print("Hi")

    def checkbox_xlsx_selected(self, instance, value):
        if value is True:
            global Cam
            Cam.op_file_format = 'xlsx'
#            print("Hello")

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)



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
#        print('The button <%s> is being pressed' % instance.id)
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
