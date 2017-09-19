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

#endregion

class CustomDropDown(BoxLayout):
    pass

class CustWidget(GridLayout):
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

class MainWidget(GridLayout):

    def __init__(self,**kwargs):
        super(MainWidget,self).__init__(**kwargs)

        def callback(instance):
            print('The button <%s> is being pressed' % instance.id)
            if instance.text=="+":
                instance.text = 'Inactive'
                i=int(instance.id[10:])
                i+=1

                self.add_widget(CustWidget(id='custwid'+str(i)))
                btn = Button(id='plusbutton'+str(i), text='+', height='52dp', size_hint=(0.07, None))
                self.add_widget(btn)
                btn.bind(on_press=callback)

        i=1
        self.add_widget(CustWidget(id='custwid'+str(i)))
        btn = Button(id='plusbutton'+str(i), text='+', height='52dp', size_hint=(0.07, None))
        self.add_widget(btn)
        btn.bind(on_press=callback)

class CPCGeApp(App):
    def build(self):
        return Builder.load_file("CPCG.kv")


App = CPCGeApp()
App.run()
