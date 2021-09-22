import csv

header = ['№ маршрута', 'Состав', 'время прибытия', 'время отбытия']
data = [
        ['8', '2708', '12:51:33', '13:13:33'],
        ['15', '1564', '14:45:11', '15:20:12'],
        ['21', '3328', '12:51:33', '13:13:33'],
        ['48', '1997', '12:51:33', '13:13:33'],
        ['135', '2228', '12:51:33', '13:13:33']
       ]

with open('wagons.csv', 'w', encoding='cp1251', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
