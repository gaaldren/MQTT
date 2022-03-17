from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

import paho.mqtt.client as mqtt
import threading

# Цвет окна
Window.clearcolor = (.9, .9, .9, 1)



        


class Container(GridLayout):

    def start_send(self):
        threading.Thread(target=self.public,daemon=True).start()
    
    def public(self):   
        broker = "test.mosquitto.org" 
        client = mqtt.Client("Device")
        client.connect(broker)
        text = self.ids.text_input.text
        
        pubtop = self.ids.spin_top.text
        
        if pubtop == 'mqtt/chat/android':
            self.ids.label_out.text = 'Вы отправили -> ' + text + '\n'
        
        if pubtop == 'Top2':
            self.ids.label_out.text = 'Select top2'
        
        if pubtop == 'Top3':
            self.ids.label_out.text = 'Select top3'
        
        client.publish(pubtop,text)
    
    def start_take(self):
        threading.Thread(target=self.take_message,daemon=True).start()
    
    def on_message(self,client,userdata,message):
        if message.topic == 'mqtt/example1':
            self.ids.label_out.text(message.topic + ' ' + message.payload.decode('utf-8') + '\n')
    
    def take_message(self):
        broker = "test.mosquitto.org"
        client = mqtt.Client()

        client.connect(broker)

        client.subscribe('mqtt/example1')
        client.loop_start()
              
        while True:
            client.on_message = self.on_message


class MyApp (App):
    def build(self):
        return Container()  

if __name__ == '__main__':
    MyApp().run()