
import paho.mqtt.client as mqtt
import time

# аргументы подлкючения
# rc 0 - conn succeeded
# rc 1 - protocl error
# rc 2 - invalid client id
# rc 3 - the server is not availiable
# rc 4 - wrong username or password
# rc 5 - unauthorized
def on_connect(client,userdata,flags,rc):
    print('Подключение дало результат ' + str(rc))



def on_message(client,userdata,message):
     #print('received message: ', str(message.payload.decode('utf-8')))
     print('Получено сообщение ' + str(message.payload) + ' от топика ' + message.topic + ' с qos '+ str(message.qos))

broker = "mqtt.eclipseprojects.io"


client = mqtt.Client('another_dev')

# qos 0  - максимальная производительность, возможна потеря
# qos 1  - гарантировано придет, но возможен дубликат 
# qos 2  - гарантировано придет, пониженная производительность 
# по умолчанию qos = 0
try:
    client.connect(broker)
    client.subscribe('examp') # метод для подписки на топик
    client.loop_start()
    client.on_connect = on_connect
    client.on_message = on_message
except Exception as err:
    print(err)
    print('Отсутствует подключение к брокеру')
#client.tls_set()
#client.username_pw_set(username = 'qwerty',password = 11)
#print('connection to a broker...')

time.sleep(10) # время выполнения в сек

client.loop_end()
