import random
from typing import Iterable, List

from hangman.game_status import GameStatus
from hangman.invalid_operation_exception import InvalidOperationError


class Game:

    def __init__(self, allowed_misses: int = 6):
        if allowed_misses < 5 or allowed_misses > 8:
            raise ValueError('a number should be between 5 and 8')

        self.__allowed_misses = allowed_misses  # возможные ошибки
        self.__tries_counter = 0  # вся эта история приватная, чтобы нельзя было модифицировать
        self.__tried_letters = []  # опробованные буквы
        self.__open_indexes = []  # еще не открытые буквы
        self.__game_status = GameStatus.NOT_STARTED  # тут энумерейт, перечисление, создали новый файл для него
        self.__word = ''

    def generate_word(self) -> str:  # указываем, что возвращается строка
        """

        :rtype: object
        """
        filename = "data\\WordsStockRus.txt"
        words = []
        with open(filename,
                  encoding='utf-8') as file:  # тут мы просто открываем файл, считываем построчно и доюавляем в список
            for line in file:
                words.append(line.strip('\n'))

        rand_index = random.randint(0, len(words) - 1)  # берем рандомный индекс
        self.__word = words[rand_index]  # берем слово по рандомному индексу

        self.__open_indexes = [False for _ in self.__word]  # по умолчанию все являются открытыми индексами
        self.__game_status = GameStatus.IN_PROGRESS  # меняем статус на в прогрессе

        return self.__word

    def guess_letter(self, letter: str) -> Iterable[str]:  # возвращаем список строк типа
        if self.tries_counter == self.allowed_misses:  # если исчерпано количество попыток, возбуждаем исключение
            # это исключение должно сообщить, что именно сам метод нельзя вызвать при текущем состоянии объекта
            raise InvalidOperationError(f'число ошибок достигло максимума. доступно {self.allowed_misses}')

        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f'статус игры находится не в прогрессе, текущий статус: {self.game_status}')

        # флаг, с помощью которого мы  трекаем, была ли открыта буква, если была, то трайс_каунтер не запускается
        open_any = False
        result: List[str] = []

        for i in range(len(self.word)):
            cur_letter = self.word[i]
            if cur_letter == letter:
                self.__open_indexes[i] = True
                open_any = True

            if self.__open_indexes[i]:
                result.append(cur_letter)
            else:
                result.append('-')

        if not open_any:
            self.__tries_counter += 1

        self.__tried_letters.append(letter)

        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.tries_counter == self.allowed_misses:
            self.__game_status = GameStatus.LOST

        return result

    def __is_winning(self):
        for cur in self.__open_indexes:
            if not cur:
                return False
        return True

    @property  # ограничение внешнего кода к нашим атрибутам
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def word(self) -> str:
        return self.__word

    @property
    def allowed_misses(self) -> int:
        return self.__allowed_misses

    @property
    def tries_counter(self) -> int:
        return self.__tries_counter

    @property
    def tried_letters(self) -> Iterable[str]:
        return sorted(self.__tried_letters)

    @property
    def remaining_tries(self) -> int:
        return self.allowed_misses - self.tries_counter
