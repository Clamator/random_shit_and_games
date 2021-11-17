with open('C:\\test\\test.txt', mode='r') as file:
    text = file.read()

    print(text.split(' '))

import psycopg2
conn = psycopg2.connect(dbname='testdb', user='postgres', password='A8nDIVDh23')
cur = conn.cursor()

cur.execute('insert into person (first_name, surname, gender, birth_date) values (%s, %s, %s, %s)', text.split(' '))
conn.commit()


print(type(text))

# нужное
#import psycopg2
#conn = psycopg2.connect(dbname='testdb', user='postgres', password='A8nDIVDh23')
#cur = conn.cursor()
#
#while True:
#    cur.execute('insert into person (first_name, surname, gender, birth_date) values (%s, %s, %s, %s)', file.read())
#
#conn.commit()
