import sqlalchemy
from sqlalchemy import Column, Integer, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:A8nDIVDh23@localhost:5432/testdb')

connection = engine.connect()

# connection.execute('insert into person (first_name, surname, gender, birth_date) values (%s, %s, %s, %s) ')



Base = declarative_base()


class Person(Base):  # это название класса, а не таблицы
    __tablename__ = 'person'  # то, как он прописан именно в БД

    #  здесь мы фактически описываем таблицу в терминах Алхимии
    person_id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    surname = Column(Text)
    gender = Column(Text)
    birth_date = Column(Date)


Base.metadata.create_all(engine)  # движок мы создавали ранее, и теперь мы готовы работать с БД.

Session = sessionmaker(bind=engine)
session = Session()

#person1 = Person(person_id=16, first_name='Kesha', surname='Ololoev', gender='male', birth_date='2020-09-14')
#session_discogs.add(person1)
#session_discogs.commit()

for item in session.query(Person).order_by(Person.birth_date):
    print(item.first_name, ' ', item.birth_date)

for item in session.query(Person).filter(Person.birth_date > '2000-01-01'):
    print(item.first_name, ' ', item.birth_date)