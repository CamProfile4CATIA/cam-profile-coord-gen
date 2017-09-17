import kivy

kivy.require("1.9.0")

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

class CustomDropDown(BoxLayout):
    pass
class CustWidget(GridLayout):
    pass

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





class MyWidget(RelativeLayout):
    box = ObjectProperty(None)

    def on_box(self, *args):
        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)
            self.box.add_widget(CustWidget())
            btn1 = Button(text='+', height='52dp',  size_hint=(0.07, None))
            self.box.add_widget(btn1)
            btn1.bind(on_press=callback)

        self.box.add_widget(CustWidget())
        btn1 = Button(text='+', height='52dp',  size_hint=(0.07, None))
        self.box.add_widget(btn1)
        btn1.bind(on_press=callback)


Factory.register('MyWidget', cls=MyWidget)




class CPCGeApp(App):
    def build(self):
        return Builder.load_file("CPCG.kv")


App = CPCGeApp()
App.run()
