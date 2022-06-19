from hangname import hangname_game
from divination import divination_game
from tictactoe import tictactoe_game


def game_center():
    print('||||||||||||||||||||||||')
    print('|WELCOME TO GAME CENTER|')
    print('||||||||||||||||||||||||')

    print('(1) Divination')
    print('(2) Hangman')
    print('(3) Tic-tac-toe')
    print('(4) Chess')

    game = input('Select a game: ')

    while game not in ['1', '2', '3', '4']:
        print('please enter a valid number.')
        game = input('Select difficulty: ')

    if game == '1':
        divination_game()
    elif game == '2':
        hangname_game()

    elif game == '3':
        print('work in progress')
    elif game == '4':
        print('work in progress')


if __name__ == '__main__':
    game_center()

