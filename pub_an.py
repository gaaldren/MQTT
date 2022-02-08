from email.mime import message
import paho.mqtt.client as mqtt
import time
from random import random, randrange, randint

broker = "mqtt.eclipseprojects.io" # объявление брокера 
try:
    client = mqtt.Client("Device") # класс mqtt с помощью метода Client дает имя Device
    client.connect(broker) # переменная client использует метод для подключение к объявленному брокеру 

    # бесконечном цикле отправление сообщения с рандомной цифрой
    while True:
        rand = randint(0,20)
        client.publish('examp',rand) # метод для публкикации сообщений брокеру в аргументе топик
        print('Отправил '+ str(rand) + ' to topic ')
        time.sleep(1)
except Exception as err:
    print(err)
    print('Отсутствует подключение к брокеру')
