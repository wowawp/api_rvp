# TODO 1) Подключиться через сокет к существующему api РВП.
# TODO 2) Послать запрос по api на получения потока данных о нахождении поезда на рельсовых цепях.
# TODO 3) Получить ответ от сервера.
# TODO 4) Обработать полученный ответ.
# TODO 5) Записать обработанный ответ в ексель таблицу/ django
import socket
import sys
import json
import time
# from csv_file import *

dict1 = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen = True

server_address = ('10.238.3.101', 2194)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
try:
    request = {'jsonrpc': '2.0',
               'method': 'addListener',
               'params':  {'lineIds': ["sllLine"],
                           'intervalMsecs': 1000},
               'id': 1}
    request = json.dumps(request)
    print('sending "%s"' % request)
    sock.sendall(bytes(request, encoding="utf-8"))
    while listen:
        time.sleep(1)
        data = sock.recv(16384)
        with open('json.json', 'w') as file:
            file.write(data.decode('utf-8'))
        a = data.decode('utf-8')
        # csv_file()
        print('received "%s"' % data.decode('utf-8'))
finally:
    print('closing socket')
    sock.close()

