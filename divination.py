import random


def divination_game():
    print('||||||||||||||||||||||||||||')
    print('|WELCOME TO DIVINATION GAME|')
    print('||||||||||||||||||||||||||||')
    print('')

    print('Easy, ten chances, from 1 to 10. Enter - 1')
    print('Medium, five chances, from 1 to 100. Enter - 2')
    print('Hard, one chance, from 1 to 1000. Enter - 3')
    print('')

    difficulty = input('Select difficulty: ')

    while difficulty not in ['1', '2', '3']:
        print('please enter a valid number.')
        difficulty = input('Select difficulty: ')

    secret_value = random.randint(1, 11 if difficulty == '1' else 101 if difficulty == '2' else 1001)
    chances = 10 if difficulty == '1' else 5 if difficulty == '2' else 1
    tempting = 0

    while tempting != chances:
        try:
            attempt = int(input(f'attempt {tempting+1}: '))
            tempting = tempting + 1
            if attempt < secret_value:
                print('wrong, try a higher number.')
            elif attempt > secret_value:
                print('wrong, try a smaller number.')
            else:
                print('CONGRATULATIONS YOU GET IT RIGHT!')
                print(f'the secret number was {secret_value}.')
                tempting = chances
        except ValueError:
            print('please enter a valid value.')
            tempting = tempting + 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    divination_game()
