import unittest 
import socket

from client_for_mqtt import *
from ui_client import Ui_MainWindow

class TestMqtt(unittest.TestCase):
    def setUp(self):
        self.client1 = MainWindow(QMainWindow)

    def TestIp(self):
        h_name = socket.gethostname()
        IP_addres = socket.gethostbyname(h_name)
        self.assertEqual(self.client1.get_ip, IP_addres)

    # def TestIp(self):
    #     h_name = socket.gethostname()
    #     IP_addres = socket.gethostbyname(h_name)
    #     self.assertEqual(self.client1.get_ip, IP_addres)
    
    
if __name__ == "__main__":
    unittest.main()