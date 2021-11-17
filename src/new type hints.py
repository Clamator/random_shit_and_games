from typing import Literal, Final, final, Dict, Any, TypedDict


# f = open(r'C:\code\onenames.py', 'r')
# a = f.read()
# print(a)


# пример: тут в метод чтения чтения можно передать что угодно, и пользователь не узнает об этом
# еслимы испортируем литерал, то в режим(это в данном случае) мы можем передать необходимые значения
# но все равно, мы хоть и указываем, что можно передать только определенные, функция работает
# но можно отлавливать такое на этапе анализа скриптов
def open_file(file, mode: Literal['r', 'w']):
    print('opening file...')


open_file(r'C:\code\onenames.py', 'r')

# констант не было, но появились такие, которые основаны на тайп хинтинге, вызывается через from typing import Final
# при попытке изменить pi мы получим уведомление о невозможности переприсвоения значения

pi: Final = 3.1415


# есть декоратор Final для классов, он запрещает наследование того класса, что покрыт декоратором
@final
class Dog:
    def init(self):
        self.legs = 4
        self.health = 100
        self.sound = 'woof'

    def bark(self):
        print(self.sound)


# все, выделен класс, как и с константой - все равно можно унаследовать и т.д, не жесткое ограничение, как навязывание
class SuperDog(Dog):
    def init(self):
        super().init()
        self.legs = 4
        self.health = 200
        self.sound = 'woof-woof'


sd = SuperDog()
print(sd.health)
print(sd.sound)

# обычно классы запечатывают, когда они реализуют фичи безопасности, а наследование может безопасности навредить
# или если класс состоит из одних статических членов, т.к. нет смысла расширять класс
# но таких случае мало, в питоне по умолчанию все классы открыты, пока нет необходимости их закрыть
# ниже указано, что словарь принимает в ключ - строку, в значение - строку
person: Dict[str, str] = {'name': 'Alex', 'surname': 'Munroe', 'sex': 'male'}

# если мы хотим передавать любое значение в значение, то надо Any

person2: Dict[str, Any] = {'name': 'Alex', 'surname': 'Munroe', 'sex': 'male', 'age': 27}

person2['age'] = 28


# теперь структуру словаря можно описать
class Human(TypedDict):
    name: str
    surname: str
    sex: str
    age: int


person3: Human = {'name': 'Alex', 'surname': 'Munroe', 'sex': 'male', 'age': 27}
