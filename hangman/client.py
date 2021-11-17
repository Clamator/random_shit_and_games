from hangman.game import Game
from hangman.game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

letters_count = len(word)

print(f'the length of word is {letters_count}')
print('try to guess word letter by letter')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('pick a letter: \n')
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f"remaining tries = {game.remaining_tries}")
    print(f'tried letters = {chars_list_to_str(game.tried_letters)}')

if game.game_status == GameStatus.LOST:
    print('you are defeated')
    print(f'the word was {game.word}')

else:
    print('Congrats. You have won')
