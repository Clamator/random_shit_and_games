import psycopg2

# ф-я коннект создает соединение с БД и возвращает результат
from psycopg2.extras import RealDictCursor, execute_values

with psycopg2.connect(dbname='testdb', user='postgres', password='A8nDIVDh23@#') as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as curs:
        execute_values(curs, 'insert into traffic_light (light) values %s', [("blue",), ("orange",)])

        curs.execute("SELECT * FROM traffic_light")
        records = curs.fetchall()
        print(records)
        print(records[0]['light'])


