import csv
import json


header = ['Line', 'Route', 'head number', 'TCS']
res = []


def csv_file():

    with open('test.json', 'r') as json_file:
        data = json.load(json_file)
        if 'params' not in data:
            print('skip')
        else:
            for p in data['params']['events']:
                data = [p['line'], p['route'], p['headNo'], p['tcs']]
                res.append(data)

    with open('wagons.csv', 'a', encoding='cp1251', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(res)
# data = [
#         ['8', '2708', '12:51:33', '13:13:33'],
#         ['15', '1564', '14:45:11', '15:20:12'],
#         ['21', '3328', '12:51:33', '13:13:33'],
#         ['48', '1997', '12:51:33', '13:13:33'],
#         ['135', '2228', '12:51:33', '13:13:33']
#        ]

csv_file()