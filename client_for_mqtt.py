from tkinter.tix import Tree
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
from email.mime import message
from typing_extensions import Self
import paho.mqtt.client as mqtt
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

import threading
import psutil
import time 
from ui_client import Ui_MainWindow

import pygame
import socket


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Клиент 1')
        self.ui.lineEdit_for_writetext.setPlaceholderText('Ввести текст для mqtt/example1')

        # self.ui.textEdit_for_view.setStyleSheet('background-color: rgb(76, 79, 84)')

        pygame.mixer.init()
        self.playing = False
        
        self.ui.textEdit_for_view.setReadOnly(True)
        self.setWindowIcon(QIcon('ico.ico'))
        self.hdd = psutil.disk_usage('/')
        self.start_take()
        self.ui.btn_for_sendmessage.clicked.connect(self.start_send)

        # массив для отправки сообщений с темой 
        list_for_publish_client_1 = [
            'mqtt/example1',
            'device/ip',
            'mqtt/picture',
            'mqtt/get_weather/temp',
            'mqtt/get_weather/status'
        ]

        self.ui.comboBox_for_select_topic.addItems(list_for_publish_client_1)
        

        # массив подписок 

        # self.pubtop = 'mqtt/example1' # для отправки 
        # self.subtop = 'mqtt/example2' # для принятия иными словами подписка
    




    def start_send(self):
        threading.Thread(target=self.public,daemon=True).start()

    def public(self):    
        text = self.ui.lineEdit_for_writetext.text()
        broker = "test.mosquitto.org" 
        client = mqtt.Client("Device")
        client.connect(broker)

        pubtop = self.ui.comboBox_for_select_topic.currentText()

        if pubtop == 'mqtt/example1':
            self.ui.textEdit_for_view.insertPlainText('Вы отправили -> ' + text + '\n')
        
        if pubtop == 'device/ip':
            h_name = socket.gethostname()
            IP_addres = socket.gethostbyname(h_name)
            self.ui.textEdit_for_view.insertPlainText('Вы отправили -> ' + IP_addres + '\n')
        
        if pubtop == 'mqtt/picture':
            self.ui.textEdit_for_view.insertPlainText('Вы отправили -> ' + 'Picture1.jpg' + '\n')
        
        if pubtop == 'mqtt/get_weather/temp':
            self.ui.textEdit_for_view.insertPlainText('Вы отправили -> ' + 'запрос на температуру' + '\n')
        
        if pubtop == 'mqtt/get_weather/status':
            self.ui.textEdit_for_view.insertPlainText('Вы отправили -> ' + 'запрос на статус погоды' + '\n')
        
        client.publish(pubtop,text)

        
        self.ui.lineEdit_for_writetext.clear()
        
    
    # ------------------------------------------------------------------------# 
 

    # def forever_potok(self): 
    #     threading.Thread(target=self.start_track,daemon=True).start()

    def start_track(self):
        pygame.mixer.music.load('Track1.mp3')
        pygame.mixer.music.play()
        self.playing = True

    def stop_track(self):
        if self.playing:
            pygame.mixer.music.pause()


    
    def start_take(self):
        threading.Thread(target=self.take_message,daemon=True).start()
    
    def on_connect(self,client,userdata,flags,rc):
        self.ui.label_for_connect_result.setText(('Подключение дало результат ' + str(rc) + '\n'))
    

    def on_message(self,client,userdata,message): 
        if message.topic == 'device/memorystatus/harddrive/c':
            self.ui.textEdit_for_view.insertPlainText(message.topic + ' ' + str(self.hdd.free / (2**30))+ '\n') 
            self.ui.textEdit_for_view.setStyleSheet('background-color: red')
            time.sleep(3)
            self.ui.textEdit_for_view.setStyleSheet(    
            'background-color: rgb(76, 79, 84);'
            'color: white;'
            'border-radius: 1px solid;')

    
        if message.topic == 'device/work/cpu':
            self.ui.textEdit_for_view.insertPlainText(message.topic + ' ' + str(psutil.cpu_percent(interval=1))+ '%' + '\n') 
            
        
        if message.topic == 'mqtt/text/chat':
            self.ui.textEdit_for_view.insertPlainText(message.topic + ' ' + message.payload.decode('utf-8') + '\n' )
        
        if message.topic == 'device/work/ram':
            values = psutil.virtual_memory().percent
            self.ui.textEdit_for_view.insertPlainText(message.topic + ' ' + str(values) + '%' + '\n')
        
        if message.topic == 'music/track1/start':
            self.ui.textEdit_for_view.insertPlainText(message.topic + '  Track1 начал проигрывание' + '\n')
            self.start_track()

        
        if message.topic == 'music/track1/stop':
            self.ui.textEdit_for_view.insertPlainText(message.topic + '  Track1 закончил проигрывание' + '\n')
            self.stop_track()

    def take_message(self):
        broker = "test.mosquitto.org"
        client = mqtt.Client()

        client.connect(broker)
        # subtop = self.list_for_take_client_1
        
        client.subscribe('device/memorystatus/harddrive/c') 
        client.subscribe('device/work/cpu')
        client.subscribe('mqtt/text/chat')
        client.subscribe('device/work/ram')
        client.subscribe('music/track1/start')
        client.subscribe('music/track1/stop')
        client.loop_start()
        
        client.on_connect = self.on_connect
        
        while True:
            client.on_message = self.on_message


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
