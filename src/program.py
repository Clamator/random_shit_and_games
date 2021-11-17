from random import random
from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Character:

    def __init__(self, armor: int, power: int):
        self.armor = armor
        self.power = power
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage
        return self.health > 0

    def __is_alive(self) -> bool:  # указываем возвращаемый тип данных
        return self.health > 0


c1 = Character(20, 20)
c1.hit(20)

speed = Optional[int]  # предпочтительно инт
attack: Any = 50  # любое   
slave: Any = "yes"
length: Union[int, float]  # несколько
lst: list  # список, но тут не говорится, что список должен содержать конкретно строки, цифры и тд
lst2: List[int]  # прием только цифр
player: Tuple[str, int]  # как должен выглядеть кортеж
players = Dict[str, int] = {'Kesha': 100}  # DefaultDict доступен также


def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)
