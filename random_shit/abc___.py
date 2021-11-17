from abc import ABC, abstractmethod
import math


class RandomShit(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def radius(self, r):
        pass


class Rand2(RandomShit):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def radius(self, r):
        return print(2 * math.pi * r**2)

    def __str__(self):
        return f' {self.r=}'


if __name__ == '__main__':
    proba = Rand2(25)
    print(proba)
    proba.radius(5)
