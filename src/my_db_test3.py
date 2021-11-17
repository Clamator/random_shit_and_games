from src.deco import measure_time

file = open('C:\\test\\words.txt', mode='r')

import psycopg2
conn = psycopg2.connect(dbname='testdb', user='postgres', password='A8nDIVDh23')
cur = conn.cursor()

@measure_time
def testing(file):
    for i in range(len(file.readlines())):
        file.seek(0)
        text = file.readline()
        cur.execute('insert into words (word) values (%s)', text.split())
        conn.commit()
        if not text:
            print('data input is done')

if __name__ == '__main__':
    testing(file)
