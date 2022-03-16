from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

# Цвет окна
Window.clearcolor = (.9, .9, .9, 1)

class Container(GridLayout):
    pass

class MyApp (App):
    def build(self):
        
        
        
        return Container()


if __name__ == '__main__':
    MyApp().run()