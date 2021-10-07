import datetime


def db(conn, trying):

    restrackchain = []
    if not 'params' in trying:
        print('skip empty')
    else:
        for data in trying['params']['events']:
            for trackchain in data['tcs']:
                restrackchain.append(trackchain)
            id = None
            line = str(data['line'])
            route = str(data['route'])
            headnum = str(data['headNo'])
            tcs = str(restrackchain.copy())
            # tcs = None
            datearrival = str(datetime.datetime.now())
            datedeparture = str(datetime.datetime.now() - datetime.timedelta(days=1))
            restrackchain.clear()
            cur = conn.cursor()
            with conn:
                with conn.cursor() as cursor:
                    conn.ping()  # reconnecting mysql
                    sql = "INSERT INTO train (id, line, route, headnum, tcs , datearrival, " \
                          "datedeparture) VALUES (%s, %s, %s, %s, %s, %s, %s) "
                    cursor.execute(sql, (id, line, route, headnum, tcs, datearrival, datedeparture))
                conn.commit()
            cur.close()





# import csv
# # import json
#
#
# header = ['Line', 'Route', 'head number', 'TCS']
# res = []
# restrackchain = []
#
# def csv_file(trying):
#     if not 'params' in trying:
#         print('skip empty')
#     else:
#         for data in trying['params']['events']:
#             for trackchain in data['tcs']:
#                 restrackchain.append(trackchain)
#             data = [data['line'], data['route'], data['headNo'], restrackchain.copy()]
#             restrackchain.clear()
#             res.append(data)
#
#     with open('wagons.csv', 'a', encoding='cp1251', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerows(res)
#
