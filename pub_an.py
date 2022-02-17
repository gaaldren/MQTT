import sys
from email.mime import message
from typing_extensions import Self
import paho.mqtt.client as mqtt
import time
from random import randint

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_publisher import Ui_pub_form

import threading


class Dialog(QDialog):
    def __init__(self,parent = None):
        super(Dialog,self).__init__(parent)

        self.ui = Ui_pub_form()
        self.ui.setupUi(self)
        self.ui.pub_message_box.setReadOnly(True)
        self.ui.pub_send_button.clicked.connect(self.start)

    def start(self):
        threading.Thread(target=self.public,daemon=True).start()
       
    def public(self):
        broker = "test.mosquitto.org" 
        client = mqtt.Client("Device")
        # client.username_pw_set('dev','222') # класс mqtt с помощью метода Client дает имя Device
        client.connect(broker)

        # переменная client использует метод для подключение к объявленному брокеру 
        # бесконечном цикле отправление сообщения с рандомной цифрой
        
        while True:
            rand = randint(0,20)
            client.publish('examp',rand) # метод для публкикации сообщений брокеру в аргументе топик
            # out = 'Отправил '+ str(rand) + ' to topic'
            self.ui.pub_message_box.insertPlainText('Издатель отправил '+ str(rand) + '\n')
            time.sleep(1)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Dialog()
	window.show()
	sys.exit(app.exec_())
            
