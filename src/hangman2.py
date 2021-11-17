from random import random
import random


class Hangman:
    def __init__(self, mistakes=10):
        self.board = []
        self.rand_word = ''
        self.mistakes = mistakes
        self.alphabet = list('abcdefghijklmnopqrstuvwxyz')


    def mistakes_num(self):
        self.mistakes = int(input('\nenter a number of available mistakes: '))
        return self.mistakes

    def mistakes_left(self):
        return self.mistakes

    def import_word(self):
        with open(r"C:\Users\User\JupyterRoot\WordsStockRus2.txt", mode='r', encoding='utf-8') as self.word_lst:
            read_word_lst = self.word_lst.readlines()
            print('the word is conceived')
        self.rand_word = random.choice(read_word_lst).strip('\n')
        splitted_word = list(self.rand_word)
        self.board = ['_' for i in splitted_word]
        for i in self.board:
            print(i, end=' ')
        return self.board, self.rand_word

    def ask_for_letter(self):
        while self.mistakes > 0:
            char = input('inter a char: ')
            if char in self.rand_word:
                for i, c in enumerate(self.rand_word):
                    if c == char:
                        self.board[i] = char
                        print(f'число ошибок: {self.mistakes}')
                        for el in self.board:
                            print(el, end=' ')
                        if '_' not in self.board:
                            print('\nYou win')
                            break
            else:
                self.mistakes -= 1
                print(f'число ошибок: {self.mistakes}')
                for el in self.board:
                    print(el, end=' ')
            if self.mistakes == 0:
                print('user has failed')
                print(self.rand_word)


game = Hangman()

print(game.import_word())
game.ask_for_letter()
# C:\Users\User\JupyterRoot\WordsStockRus.txt
