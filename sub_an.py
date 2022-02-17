import sys
from tracemalloc import start
from typing_extensions import Self
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import paho.mqtt.client as mqtt
import time
import socket
from ui_subscriber import Ui_sub_form

import threading
from typing_extensions import Self


class Dialog_sub(QDialog):
        def __init__(self,parent = None):
            super(Dialog_sub,self).__init__(parent)


            self.ui = Ui_sub_form()
            self.ui.setupUi(self)
            self.ui.textEdit.setReadOnly(True)
            self.start()
            self.drawIvent()
    
        
        def start(self):
            threading.Thread(target=self.take_message,daemon=True).start()

        def on_connect(self,client,userdata,flags,rc):
            self.ui.label_for_connect_result.setText(('Подключение дало результат ' + str(rc) + '\n'))

        def on_message(self,client,userdata,message):
            self.ui.textEdit.insertPlainText('Получено сообщение ' + str(message.payload.decode('utf-8')) + ' от топика ' + message.topic + ' с qos '+ str(message.qos) + '\n')
            
        
        
        def take_message(self):
            try:
                broker = "test.mosquitto.org"
                client = mqtt.Client('another_dev')

                client.connect(broker)
                client.subscribe('examp') 
                client.loop_start()
                
                client.on_connect = self.on_connect
                client.on_message = self.on_message


            except socket.error as socketerror:
                QMessageBox.warning(QMessageBox(), 'Ошибка' , str(socketerror))
        
        def drawIvent(self):
            if (self.ui.textEdit.toPlainText() == 'Издатель отправил '):
                self.setStyleSheet('background-color: red')
            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dialog_sub()
    window.show()
    sys.exit(app.exec_())


        # аргументы подлкючения
        # rc 0 - conn succeeded
        # rc 1 - protocl error
        # rc 2 - invalid client id
        # rc 3 - the server is not availiable
        # rc 4 - wrong username or password
        # rc 5 - unauthorized
