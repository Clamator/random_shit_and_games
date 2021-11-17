# подсказка линтеру, т.н. дак тайпинг, утиная типизация, означает, что сам объект менее важем, чем его тип
# если что-то крякает как утка, плавает как утка и т.л. как утка - это утка
from typing import Protocol, List


class Bird:
    def fly(self):
        print('flying with wings')


class Airplane:
    def fly(self):
        print('flying with fuel')


class Flyable(Protocol):  # вот тут создается класс, унаследованный от протокола,
    def fly(self): ...  # просто метод, который никак не реализован


def process_flyables(flyables: List[Flyable]):  # тут передаем, что передаваемый список реализует протокол Flyable(имеют метод fly)
    for cur_obj in flyables:
        cur_obj.fly()  # когда мы ставим точку, мы не видим метод флай сразу


class Fish:
    def swim(self):
        print('fish is swimming')


# в выводе у нас будут экземпляры разного типа, но у них одинаковый метод, поэтому это работает
# это и есть утиная типизация
process_flyables([Bird(), Airplane(), Fish()])  # а тут фиш должен был быть подсвечен

# какая мб проблема, если в классе нет метода флай,
# можно обусловиться, что то, что передается в flyables должно подчиняться некоторому протоколу,
# а именно должно реализовывать метод fly, и соответственно заставить линтеры проверять это
# мы создаем класс Flyable, унаследованный от Protocol, создаем там метод fly и передаем в него ..., т.е. никак не реализуем его

