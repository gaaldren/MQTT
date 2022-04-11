import requests
try:
    requests.get('http://localhost:8000')
    print("Подключение установлено")
except:
    print("Подключение не установлено")