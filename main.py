# TODO 1) Подключиться через сокет к существующему api РВП.
# TODO 2) Послать запрос по api на получения потока данных о нахождении поезда на рельсовых цепях.
# TODO 3) Получить ответ от сервера.
# TODO 4) Обработать полученный ответ.
# TODO 5) Записать обработанный ответ в ексель таблицу/ django
import socket
import json
from csv_file import *
import time
# , 'aplLine', 'krlLine'
request = {'jsonrpc': '2.0',
           'method': 'addListener',
           'params':  {'lineIds': ['sllLine'],
                       'intervalMsecs': 1000},
           'id': 1}
approved = {'jsonrpc': '2.0',
            'result': {},
            'id': 1}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.238.3.101', 2194)
sock.connect(server_address)
print('connected to %s port %s' % server_address)
listen = True

try:
    request = json.dumps(request)
    approved = json.dumps(approved)
    print('sending "%s"' % request)
    sock.sendall(bytes(request, encoding="utf-8"))
    while listen:
        data = sock.recv(8192)
        sock.sendall(bytes(approved, encoding="utf-8"))
        if len(data) == 0:
            print('WTF!!!')
        else:
            try:
                trying = json.loads(data)
                print(trying)
                # with open('json.json', 'w') as file:
                #     file.write(trying)
                #     print('received "%s"' % data.decode('utf-8'))
                csv_file(trying)

            except ValueError as e:
                pass

finally:
    print('closing socket')
    sock.close()
