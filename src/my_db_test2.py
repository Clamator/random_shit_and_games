file = open('C:\\test\\test2.txt', mode='r')

import psycopg2
conn = psycopg2.connect(dbname='testdb', user='postgres', password='A8nDIVDh23')
cur = conn.cursor()

for i in range(len(file.readlines())):
    file.seek(0)
    text = file.readline()
    cur.execute('insert into person (first_name, surname, gender, birth_date) values (%s, %s, %s, %s)', text.split())
    conn.commit()
    if not text:
        print('data input is done')
