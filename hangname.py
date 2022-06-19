from words_for_hangman import words


def hangname_game():
    print('||||||||||||||||||||||||||')
    print('|WELCOME TO HANGNAME GAME|')
    print('||||||||||||||||||||||||||')
    print('')

    print('Easy, twenty chances: 1')
    print('Medium, ten chances: 2')
    print('Hard, five chance: 3')
    print('')

    difficulty = input('Select difficulty: ')

    while difficulty not in ['1', '2', '3']:
        print('please enter a valid number.')
        difficulty = input('Select difficulty: ')

    secret_name = words().lower()
    sorted_secret_name = sorted(set(list(secret_name)))

    chances = 20 if difficulty == '1' else 10 if difficulty == '2' else 5
    size_name = len(secret_name)

    letter_list = []
    secret_line = '  '
    letters_line = '  '

    while sorted(list(set(letter_list).intersection(sorted_secret_name))) != sorted_secret_name:

        if chances > 0:

            for character in secret_name:
                secret_line = secret_line + '_  '

                if character in letter_list:
                    letters_line = letters_line + f'{character}  '

                else:
                    letters_line = letters_line + '*  '

            print(f'the word has {size_name} letters! Remaining chances: {chances}')
            print('---------------------------------')
            print(letters_line)
            print(secret_line)
            print('---------------------------------')
            print('')

            letter = input('type one character: ')

            while len(letter) != 1:
                print('Please type only one character at a time.')
                letter = input('type one character: ')

            while len(letter) in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('Please enter a letter, not a number.')
                letter = input('type one character: ')

            letter_list.append(letter)
            letters_line = '  '
            secret_line = '  '
            chances = chances - 1

        else:
            print('|||||||||||||||||||||||||')
            print('|       YOU LOSE!       |')
            print('|||||||||||||||||||||||||')
            print('')
            print(f"the animal's name was: {secret_name}")
            letter_list = sorted_secret_name

        if sorted(list(set(letter_list).intersection(sorted_secret_name))) == sorted_secret_name and chances > 0:
            print('|||||||||||||||||||||||||')
            print('|       YOU WIN!        |')
            print('|||||||||||||||||||||||||')
            letter_list = sorted_secret_name


if __name__ == '__main__':
    hangname_game()
