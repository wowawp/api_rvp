# TODO 1) Подключиться через сокет к существующему api РВП.
# TODO 2) Послать запрос по api на получения потока данных о нахождении поезда на рельсовых цепях.
# TODO 3) Получить ответ от сервера.
# TODO 4) Обработать полученный ответ.
# TODO 5) Записать обработанный ответ в ексель таблицу/ django
import socket
import sys
import json


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen = True

server_address = ('10.238.3.101', 2194)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
try:
    # j = {"jsonrpc": "2.0","method": "listLines","id": 1}
    # query = '{"jsonrpc": "2.0","method": "listLines","id": 1}'
    request = {'jsonrpc': '2.0', 'method': 'addListener', 'params':  {'lineIds': ["sllLine"], 'intervalMsecs': 1000}, 'id': 1}

    request = json.dumps(request)
    print('sending "%s"' % request)
    while listen:
        sock.sendall(bytes(request, encoding="utf-8"))

        data = sock.recv(8760)
        # amount_received += len(data)
        with open('line.txt', 'a') as file:
            file.write(data.decode('utf-8'))
        a = data.decode('utf-8')
        # da = json.loads(a)
        # if 'name' in da['items'] and da['items']['name'].lower() == 'scarf':
        #     print'There is Scarf'
        print('received "%s"' % data.decode('utf-8'))

finally:
    print('closing socket')
    sock.close()
