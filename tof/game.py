from tof.status_game import StatusGame


class Game:

    def __init__(self, allowed_misses: int = 6):
        if allowed_misses < 5 or allowed_misses > 8:
            raise ValueError('a number should be between 5 and 8')
        self.__tup_lst = []
        self.__quest = ''
        self.__ans = ''
        self.__desc = ''
        self.__iter_list = []
        self.__allowed_misses = allowed_misses  # возможные ошибки
        self.__line = []  # это строка с в/о/п
        self.__status_game = StatusGame.NOT_STARTED

    def create_tup_lst(self):  # эта ф-я просто генерирует список кортежей, как если бы я хотел просто передать файл
        filename = "data\\Questions.csv"  # это сам файл непосредственно
        lines = []
        lst = []
        with open(filename,
                  encoding='utf-8') as file:  # тут мы просто открываем файл, считываем построчно и доюавляем в список
            for line in file:
                lines.append(line.strip('\n'))

            for el in lines:
                lst.append(el.split(';'))
        self.__tup_lst = [tuple(i) for i in lst]  # список кортежей
        print('Tuple list was created')
        return self.__tup_lst

    def generate_next_qad(self):  # эта ф-я будет принимать список кортежей и йилдить три элемента, а мб сделать так, чтобы делил на линии
        print('quest line was created')  # тут мы получаем список кортежей

        self.__allowed_misses = int(input('pick a number of mistakes: '))
        self.__status_game = StatusGame.IN_PROGRESS
        mistakes = 0
        for _ in range(self.__allowed_misses):
            self.__iter_list = iter(self.__tup_lst)
            for quest, ans, desc in self.__tup_lst:
                self.__quest = quest
                self.__ans = ans
                self.__desc = desc

                ready = input("are you ready for the next question?: ")
                if ready != "Yes":
                    continue
                print(self.__quest)
                print("your answer is?: ")
                answer = input()
                if answer == self.__ans:
                    print("right")
                    print(self.__desc)
                    next(self.__iter_list)
                elif answer != self.__ans:
                    mistakes += 1
                    print("wrong answer")
                    print(self.__desc)
                    next(self.__iter_list)

                if mistakes == self.__allowed_misses:
                    self.__status_game = StatusGame.LOST
                    print('\n you are loser, game over')
                    break
