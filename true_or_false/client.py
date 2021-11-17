from true_or_false.game import Game
from true_or_false.game_result import GameResult
from true_or_false.game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f'questions asked: {result.questions_passed}. Mistakes made: {result.mistakes_made}')
    print(f'you won' if result.won else 'You lost')


game = Game('data\\Questions.csv', end_of_game_handler, allowed_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:
    q = game.get_next_question()
    print(f'the next question is: {q.text}')
    answer = input() == 'y'
    if q.is_true == answer:
        print('OK')
    else:
        print('you are mistaken')
        print(q.explanation)
    game.give_answer(answer)
