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

from plyer import vibrator, tts
import paho.mqtt.client as mqtt
import threading
import http.client


Window.clearcolor = (.9, .9, .9, 1)


class Container(GridLayout):
    def __init__(self):
        super(Container, self).__init__()
        self.client = mqtt.Client()
        self.client.connect("test.mosquitto.org")
        self.take_message(self.client)

    def start_send(self):
        threading.Thread(target=self.public(self.client), daemon=True).start()

    def public(self, client):
        text = self.ids.text_input.text
        pubtop = self.ids.spin_top.text

        if pubtop == 'mqtt/chat/client_1/android':
            self.ids.label_out.text = 'Вы отправили -> ' + text + '\n'
            self.client.publish(pubtop, text)

        if pubtop == 'mqtt/pc/client_1/restart':
            self.ids.label_out.text = 'Вы отправили -> <Перезагрузка>'
            self.client.publish(pubtop)

        if pubtop == 'mqtt/file/client_1/get_text':
            self.ids.label_out.text = 'Вы отправили -> <ASCII> '
            self.client.publish(pubtop)

        if pubtop == 'mqtt/browser/client_2/open':
            self.ids.label_out.text = 'Вы отправили -> <Открыть браузер> '
            self.client.publish(pubtop)

        if pubtop == 'mqtt/pc/client_2/get_screen':
            self.ids.label_out.text = 'Вы отправили -> <Сделать скриншот> '
            self.client.publish(pubtop)

        if pubtop == 'android/get_ip/return':
            self.ids.label_out.text = 'Вы отправили -> <Возврат ip> ' + '\n'

    def get_ascii(self):
        self.ids.label_out.text = (

            ' __    __     ______     ______   ____ \n'
            '/\ "-./  \   /\  __ \   /\__  _\ /\__  _\  \n'
            '\ \ \-./\ \  \ \ \/\_\  \/_/\ \/ \/_/\ \/  \n'
            ' \ \_\ \ \_\  \ \___\_\    \ \_\    \ \_\  \n'
            '  \/_/  \/_/   \/___/_/     \/_/     \/_/  \n'
            + '\n'

            + '\n'
        )

    def on_message(self, client, userdata, message):
        if message.topic == 'mqtt/example1':
            self.ids.label_out.text = message.topic + \
                '  ' + message.payload.decode('utf-8')

        if message.topic == 'android/get_ip':
            conn = http.client.HTTPConnection("ifconfig.me")
            conn.request("GET", "/ip")
            out = conn.getresponse().read()
            self.ids.label_out.text = str(out)
            self.client.publish('android/get_ip/return', out)

        if message.topic == 'android/get_ascii':
            self.get_ascii()

        if message.topic == 'android/vibro':
            vibrator.vibrate(3)

        if message.topic == 'android/tts':
            tts.speak('Hello friend')

    def take_message(self, client):
        self.client.subscribe('mqtt/example1')
        self.client.subscribe('android/get_ip')
        self.client.subscribe('android/vibro')
        self.client.subscribe('android/get_ascii')
        self.client.subscribe('android/tts')
        self.client.loop_start()

        client.on_message = self.on_message


class MyApp (App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
