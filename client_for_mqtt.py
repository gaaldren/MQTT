from tkinter.tix import Tree
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import os
import sys
from email.mime import message
from typing_extensions import Self
import paho.mqtt.client as mqtt
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

from datetime import datetime
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

        
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_ghost.clicked.connect(lambda: self.showMinimized())


        self.ui.lineEdit_for_writetext.setPlaceholderText('Ввести текст для mqtt/example1')
        self.ui.textEdit_for_view.setPlaceholderText( 'Здесь отображаются сообщения ' + '\n'
      ' __    __     ______     ______   __     \n'
      '/\ -./  \   /\  __ \   /\__  _\ /\__  _\  \n'
      '\ \ \-./\ \  \ \ \/\_\  \/_/\ \/ \/_/\ \/  \n'
      ' \ \_\ \ \_\  \ \___\_\    \ \_\    \ \_\  \n'
      '  \/_/  \/_/   \/___/_/     \/_/     \/_/  \n'
        + '\n')
        self.ui.pushButton_page1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_page2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui._old_pos = None
        self.center()
        
        self.client = mqtt.Client()
        self.client.connect("test.mosquitto.org")
        self.start_take()

        pygame.mixer.init()
        self.playing = False

        
        self.ui.textEdit_for_view.setReadOnly(True)
        self.hdd = psutil.disk_usage('/')
        self.ui.btn_for_sendmessage.clicked.connect(self.start_send)

        list_for_publish_client_1 = [
            'mqtt/example1',
            'device/ip',
            'mqtt/picture',
            'mqtt/get_weather/temp',
            'mqtt/get_weather/status',
            'android/vibro',
        ]

        self.ui.comboBox_for_select_topic.addItems(list_for_publish_client_1)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()


    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass



    def start_send(self):
        threading.Thread(target=self.public(self.client),daemon=True).start()

    def public(self,client):  
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")  
        text = self.ui.lineEdit_for_writetext.text()


        pubtop = self.ui.comboBox_for_select_topic.currentText()
        
        if pubtop == 'android/vibro':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + '<вибрация> ' + '\n')

        if pubtop == 'mqtt/example1':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' +'<' + text + '> ' + '\n')
        
        if pubtop == 'device/ip':
            h_name = socket.gethostname()
            IP_addres = socket.gethostbyname(h_name)
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + '<' + IP_addres + '> '+ '\n')
        
        if pubtop == 'mqtt/picture':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + '<Picture1.jpg> ' + '\n')
        
        if pubtop == 'mqtt/get_weather/temp':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + '<запрос на температуру> ' + '\n')
        
        if pubtop == 'mqtt/get_weather/status':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + '<запрос на статус погоды> ' + '\n')
        
                    
        
        self.client.publish(pubtop,text)

        
        self.ui.lineEdit_for_writetext.clear()
        

    def start_track(self):
        pygame.mixer.music.load('Track1.mp3')
        pygame.mixer.music.play()
        self.playing = True

    def stop_track(self):
        if self.playing:
            pygame.mixer.music.pause()

    def start_take(self):
        threading.Thread(target=self.take_message(self.client),daemon=True).start()

    def restart(self): 
        os.system("shutdown /r /t 1")
    
    def get_ascii(self):
        self.ui.textEdit_for_view.insertPlainText(
    
' __    __     ______     ______   ____ \n'
'/\ "-./  \   /\  __ \   /\__  _\ /\__  _\  \n'
'\ \ \-./\ \  \ \ \/\_\  \/_/\ \/ \/_/\ \/  \n'
' \ \_\ \ \_\  \ \___\_\    \ \_\    \ \_\  \n'
'  \/_/  \/_/   \/___/_/     \/_/     \/_/  \n'
 + '\n' 

+ '\n' + '\n'
 )
    
    def on_message(self,client,userdata,message): 
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")


        if message.topic == 'device/memorystatus/harddrive/c':
            self.ui.textEdit_for_view.insertPlainText(message.topic + ' ' + str(self.hdd.free / (2**30))+ '\n') 
            self.ui.textEdit_for_view.setStyleSheet('background-color: red')
            time.sleep(3)
            self.ui.textEdit_for_view.setStyleSheet(    
            'background-color: rgb(76, 79, 84);'
            'color: white;'
            'border-radius: 1px solid;')

    
        if message.topic == 'device/work/cpu':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + str(psutil.cpu_percent(interval=1))+ '%' + '\n') 
            
        
        if message.topic == 'mqtt/text/chat':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + message.payload.decode('utf-8') + '\n' )
        
        if message.topic == 'device/work/ram':
            values = psutil.virtual_memory().percent
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + str(values) + '%' + '\n')
        
        if message.topic == 'music/track1/start':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + message.topic + '  Track1 начал проигрывание' + '\n')
            self.start_track()

        if message.topic == 'music/track1/stop':
            self.ui.textEdit_for_view.insertPlainText( '['+ cur_time + '] '+ message.topic + '  Track1 закончил проигрывание' + '\n')
            self.stop_track()
        
        if message.topic == 'mqtt/chat/client_1/android':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + message.payload.decode('utf-8') + '\n' )

        if message.topic == 'mqtt/pc/client_1/restart': 
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + '<Перезагрузка> ' + '\n' )
            self.restart()
        
        if message.topic == 'mqtt/file/client_1/get_text':
            self.ui.textEdit_for_view.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + '<Получить ascii> ' + '\n' + '\n' )
            self.get_ascii()
            

    def take_message(self,client):
        self.client.subscribe('device/memorystatus/harddrive/c') 
        self.client.subscribe('device/work/cpu')
        self.client.subscribe('mqtt/text/chat')
        self.client.subscribe('device/work/ram')
        self.client.subscribe('music/track1/start')
        self.client.subscribe('music/track1/stop')
        self.client.subscribe('mqtt/chat/client_1/android')
        self.client.subscribe('mqtt/pc/client_1/restart')
        self.client.subscribe('mqtt/file/client_1/get_text')

        self.client.loop_start()
        
        client.on_message = self.on_message


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
