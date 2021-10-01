import csv
import json


header = ['Line', 'Route', 'head number', 'TCS']
res = []


def csv_file():
    with open('json.json', 'r') as file:
        data = json.load(file)
        if not 'events' in data or len(data['events']) == 0:
            print('skip empty')
        else:
            for p in data['params']['events']:
                data = [p['line'], p['route'], p['headNo'], p['tcs']]
                res.append(data)

    with open('wagons.csv', 'a', encoding='cp1251', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(res)

