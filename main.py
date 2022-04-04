import speedtest
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.clock import mainthread

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import paho.mqtt.client as mqtt
import threading
import http.client
import geojson
import requests
import urllib3
import chardet
import charset_normalizer
import idna


# Цвет окна
Window.clearcolor = (.9, .9, .9, 1)


class Container(GridLayout):
    def __init__(self):
        super(Container,self).__init__()
        self.take_message()

    def start_send(self):
        threading.Thread(target=self.public,daemon=True).start()
    
    def public(self):   
        broker = "test.mosquitto.org" 
        client = mqtt.Client("Device")
        client.connect(broker)
        text = self.ids.text_input.text
        
        pubtop = self.ids.spin_top.text
        
        if pubtop == 'mqtt/chat/client_1/android':
            self.ids.label_out.text = 'Вы отправили -> ' + text + '\n'
        
        if pubtop == 'mqtt/pc/client_1/restart':
            self.ids.label_out.text = 'Вы отправили -> <Перезагрузка>'
        
        if pubtop == 'mqtt/file/client_1/get_text':
            self.ids.label_out.text = 'Вы отправили -> <ASCII> '
        
        if pubtop == 'mqtt/browser/client_2/open':
            self.ids.label_out.text = 'Вы отправили -> <Открыть браузер> '
        
        if pubtop == 'mqtt/pc/client_2/get_screen':
            self.ids.label_out.text = 'Вы отправили -> <Сделать скриншот> '
        
        client.publish(pubtop,text)
    
    # def start_take(self):
    #     threading.Thread(target=self.take_message,daemon=True).start()
    def sunrise_sunset(self):
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm =  OWM('472d111f15c9d5266faa15de9a0bc03c', config_dict)
        place = 'Киров'
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        weather = observation.weather
        sunrise = weather.sunrise_time(timeformat ='iso')
        sunset = weather.sunset_time(timeformat = 'iso')
        self.ids.label_out.text = 'Восход: ' + str(sunrise) + '\n'+ 'Закат: ' + str(sunset)

    def get_ascii(self):
        self.ids.label_out.text = (
# '-------------------------------------- ' + '\n'
    
' __    __     ______     ______   ____ \n'
'/\ "-./  \   /\  __ \   /\__  _\ /\__  _\  \n'
'\ \ \-./\ \  \ \ \/\_\  \/_/\ \/ \/_/\ \/  \n'
' \ \_\ \ \_\  \ \___\_\    \ \_\    \ \_\  \n'
'  \/_/  \/_/   \/___/_/     \/_/     \/_/  \n'
 + '\n' 
# '-------------------------------------- ' + '\n' 
 + '\n'
        )    
    # @mainthread    
    def on_message(self,client,userdata,message):
        if message.topic == 'mqtt/example1':
            self.ids.label_out.text = message.topic + '  ' + message.payload.decode('utf-8')
        
        if message.topic == 'android/get_ip':
            conn = http.client.HTTPConnection("ifconfig.me")
            conn.request("GET", "/ip")
            out = conn.getresponse().read()
            self.ids.label_out.text = str(out)


        if message.topic == 'android/get_download':
            test = speedtest.Speedtest()
            download = test.download()
            download = round((download / 1024)/1024,2)
            self.ids.label_out.text = message.topic + ' ' + str(download)
        
        if message.topic == 'android/get_ascii':
            self.get_ascii()
        
        if message.topic == 'android/sunrise_sunset':
            self.sunrise_sunset()
        
        if message.topic == 'android/get_ip/return':
            conn = http.client.HTTPConnection("ifconfig.me")
            conn.request("GET", "/ip")
            out = conn.getresponse().read()
            broker = "test.mosquitto.org" 
            client = mqtt.Client("Device")
            client.connect(broker)
            client.publish('mqtt/example1',out)

    def take_message(self):
        broker = "test.mosquitto.org"
        client = mqtt.Client()

        client.connect(broker)

        client.subscribe('mqtt/example1')
        client.subscribe('android/get_ip')
        client.subscribe('android/get_download')
        client.subscribe('android/get_ascii')
        client.subscribe('android/sunrise_sunset')
        client.subscribe('android/get_ip/return')
        client.loop_start()
              
        
        client.on_message = self.on_message

        
class MyApp (App):
    def build(self):
        return Container()  

if __name__ == '__main__':
    MyApp().run()