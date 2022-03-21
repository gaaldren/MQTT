from re import sub
import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pyautogui 
import webbrowser
from datetime import datetime
import sys
from email.mime import message
from typing_extensions import Self
import paho.mqtt.client as mqtt
import time
import socket
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import threading

import psutil

from ui_client2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Клиент 2')
        self.ui.lineEdit_for_writetext2.setPlaceholderText('Ввести текст для mqtt/text/chat')

        self.start_take()
        self.ui.btn_for_sendmessage2.clicked.connect(self.start_send)
        self.ui.textEdit_for_view2.setReadOnly(True)


        self.hdd = psutil.disk_usage('/')

        # массив для отправки сообщений с темой
        list_for_publish = [
            'mqtt/text/chat',
            'device/memorystatus/harddrive/c',
            'device/work/cpu',
            'device/work/ram',
            'music/track1/start',
            'music/track1/stop'
        ]

        self.ui.comboBox_for_select_topic2.addItems(list_for_publish)

        # self.pubtop = 'mqtt/example1' # для принятия иными словами подписка
        # self.subtop = 'mqtt/example2' # для отправки 

        # массив подписок 

    def start_send(self):
        threading.Thread(target=self.public,daemon=True).start()

    def public(self):
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")
        text = self.ui.lineEdit_for_writetext2.text()
        broker = "test.mosquitto.org" 
        client = mqtt.Client("Device")
        client.connect(broker)

        subtop = self.ui.comboBox_for_select_topic2.currentText()

        if subtop == 'device/memorystatus/harddrive/c':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<'+ str(self.hdd.free / (2**30)) + '> ' + '\n')
        
        if subtop == 'device/work/cpu':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<'+ str(psutil.cpu_percent(interval=1)) + '> ' + '%' + '\n')
        
        if subtop == 'mqtt/text/chat':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<mqtt/text/chat>  '+ text + '\n')
        
        if subtop == 'device/work/ram':
            values = psutil.virtual_memory().percent
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<'+str(values) + '> '+ '%' + '\n')
        
        if subtop == 'music/track1/start':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<команду старт для Track1> ' + '\n')
        
        if subtop == 'music/track1/stop':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<команду стоп для Track1> ' + '\n')

        
        client.publish(subtop,text)

        
        self.ui.lineEdit_for_writetext2.clear()
        
    
    # ------------------------------------------------------------------------# 



    # def start_take_picture(self):
    #     threading.Thread(target=self.take_picture,daemon=True).start()
    
    def start_take(self):
        threading.Thread(target=self.take_message,daemon=True).start()

    def take_picture(self):
        msg = QMessageBox()
        msg.setWindowTitle('Кролик')
        msg.setIconPixmap('krolik.jpg')
        msg.exec()

        # self.ui.textEdit_for_view2.clear()
    
    # def forever_take_picture(self):
    #     threading.Thread(target=self.take_picture,daemon=True).start()

    def weather(self):
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm =  OWM('472d111f15c9d5266faa15de9a0bc03c', config_dict)
        place = 'Киров'
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        weather = observation.weather
        temp = weather.temperature('celsius')['temp']
        status = weather.detailed_status
        return temp,status

        
    def on_connect(self,client,userdata,flags,rc):
        self.ui.label_for_connect_result2.setText(('Подключение дало результат ' + str(rc) + '\n'))

    def on_message(self,client,userdata,message):
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")
        if message.topic == 'mqtt/example1':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + message.payload.decode('utf-8') + '\n')
        
        if message.topic == 'device/ip':
            h_name = socket.gethostname()
            IP_addres = socket.gethostbyname(h_name)
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + IP_addres + '\n')
        
        if message.topic == 'mqtt/picture':
            self.take_picture()
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + '\n')
        
        if message.topic == 'mqtt/get_weather/temp':
            temp,status = self.weather()
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] '+ message.topic + ' ' + str(temp) + '°' + '\n')
        
        if message.topic == 'mqtt/get_weather/status':
            temp,status = self.weather()
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + str(status) + '\n')
        
        if message.topic == 'mqtt/browser/open':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + '<Браузер>' + '\n')
            webbrowser.open_new_tab('https://www.vyatsu.ru')
        
        if message.topic == 'mqtt/pc/get_screen':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + '<Скриншот>' + '\n')
            image = pyautogui.screenshot()
            image.save('screen.png')
    
    def take_message(self):
        broker = "test.mosquitto.org"
        client = mqtt.Client()

        client.connect(broker)
        client.subscribe('mqtt/example1') 
        client.subscribe('device/ip')
        client.subscribe('mqtt/picture')
        client.subscribe('mqtt/get_weather/temp')
        client.subscribe('mqtt/get_weather/status')
        client.subscribe('mqtt/browser/open')
        client.subscribe('mqtt/pc/get_screen')

        client.loop_start()
        
        client.on_connect = self.on_connect

        while True:
            client.on_message = self.on_message

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())