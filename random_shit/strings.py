from random_shit.kompPopa import Popa, Nums


class Hueta:

    def __init__(self):
        self.__canal = 1
        self.__telik = True
        self.__kompik = 3
        self.__status = 1

    def ispolnenie(self):
        popka = Popa(self.__kompik, self.__telik, self.__canal)

        if popka.telek:
            print('efsese')
            self.__status = Nums.IN_PROGRESS
            print(f'{self.__status}')

if __name__ == '__main__':
    print('started main')
    huetation = Hueta()
    huetation.ispolnenie()

