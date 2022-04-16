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
        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_ghost_w.clicked.connect(lambda: self.showMinimized())
        self.ui.lineEdit_for_writetext2.setPlaceholderText('Ввести текст для mqtt/text/chat')
        self.ui.textEdit_for_view2.setPlaceholderText( 'Здесь отображаются сообщения ' + '\n'
      ' __    __     ______     ______   _     \n'
      '/\ -./  \   /\  __ \   /\__  _\ /\__  _\  \n'
      '\ \ \-./\ \  \ \ \/\_\  \/_/\ \/ \/_/\ \/  \n'
      ' \ \_\ \ \_\  \ \___\_\    \ \_\    \ \_\  \n'
      '  \/_/  \/_/   \/___/_/     \/_/     \/_/  \n'
        + '\n')
        self.ui.pushButton_page1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_page2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        self.client = mqtt.Client()
        self.client.connect("test.mosquitto.org")

        self.start_take()
        
        self.ui.btn_for_sendmessage2.clicked.connect(self.start_send)
        self.ui.textEdit_for_view2.setReadOnly(True)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui._old_pos = None
        self.center()

        self.hdd = psutil.disk_usage('/')

        list_for_publish = [
            'mqtt/text/chat',
            'device/memorystatus/harddrive/c',
            'device/work/cpu',
            'device/work/ram',
            'music/track1/start',
            'music/track1/stop',
            'android/get_ascii',
            'android/get_ip',
            'android/tts'
        ]

        self.ui.comboBox_for_select_topic2.addItems(list_for_publish)

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
        text = self.ui.lineEdit_for_writetext2.text()


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
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<команда старт для Track1> ' + '\n')
        
        if subtop == 'music/track1/stop':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<команда стоп для Track1> ' + '\n')
        
        if subtop == 'android/get_ascii':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<запрос на ascii> ' + '\n')
        
        if subtop == 'android/get_ip':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<запрос на ip> ' + '\n')
        
        if subtop == 'android/tts':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + '<запрос на речь> ' + '\n')

        
        self.client.publish(subtop,text)

        
        self.ui.lineEdit_for_writetext2.clear()
        
    
    def start_take(self):
        threading.Thread(target=self.take_message(self.client),daemon=True).start()

    def take_picture(self):
        msg = QMessageBox()
        msg.setWindowTitle('Кролик')
        msg.setIconPixmap('krolik.jpg')
        msg.exec()
    
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
        
        if message.topic == 'mqtt/browser/client_2/open':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + '<Браузер>' + '\n')
            webbrowser.open_new_tab('https://www.vyatsu.ru')
        
        if message.topic == 'mqtt/pc/client_2/get_screen':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + '<Скриншот>' + '\n')
            image = pyautogui.screenshot()
            image.save('screen.png')
        
        if message.topic == 'android/get_ip/return':
            self.ui.textEdit_for_view2.insertPlainText('['+ cur_time + '] ' + message.topic + ' ' + message.payload.decode('utf-8') + '\n')

    
    def take_message(self,client):
        # client.connect("localhost")
        self.client.subscribe('mqtt/example1') 
        self.client.subscribe('device/ip')
        self.client.subscribe('mqtt/picture')
        self.client.subscribe('android/get_ip/return')
        self.client.subscribe('mqtt/get_weather/temp')
        self.client.subscribe('mqtt/get_weather/status')
        self.client.subscribe('mqtt/browser/client_2/open')
        self.client.subscribe('mqtt/pc/client_2/get_screen')


        self.client.loop_start()
        client.on_message = self.on_message

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())