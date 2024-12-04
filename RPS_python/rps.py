import random

def main():
    user_life = 3
    computer_life = 3
    game_count = 0

    while game_count < 3:

        user_choice = get_user_input()
        computer_choice = get_random_number()

        if computer_choice == 1:
            computer_choice = 'paper'
        elif computer_choice == 2:
            computer_choice = 'scissors'
        elif computer_choice == 3:
            computer_choice = 'rock'

        if user_choice == computer_choice:
            print(f'Computer chose: {computer_choice}')
            print('Draw')
            print('.' * 20)
            game_count += 1
        elif user_choice == 'paper' and computer_choice == 'rock':
            print(f'Computer chose: {computer_choice}')
            print('rock beats paper, computer won this round')
            print('.' * 20)
            game_count += 1
            user_life -= 1
        elif user_choice == 'scissors' and computer_choice == 'rock':
            print(f'Computer chose: {computer_choice}')
            print('rock beats scissors, computer won this round')
            print('.' * 20)
            game_count += 1
            user_life -= 1
        elif user_choice == 'rock' and computer_choice == 'paper':
            print(f'Computer chose: {computer_choice}')
            print('rock beats paper, you won this round')
            print('.' * 20)
            game_count += 1
            computer_life -= 1
        elif user_choice == 'paper' and computer_choice == 'scissors':
            print(f'Computer chose: {computer_choice}')
            print('scissors beats paper, computer won this round')
            print('.' * 20)
            game_count += 1
            user_life -= 1
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print(f'Computer chose: {computer_choice}')
            print('sciccors beats paper, you won this round')
            print('.' * 20)
            game_count += 1
            computer_life -= 1
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print(f'Computer chose: {computer_choice}')
            print('rock beats scissors, you won this round')
            print('.' * 20)
            game_count += 1
            computer_life -= 1

    print('-' * 20)
    print(f"""
        Your life = {user_life}
        Computer life = {computer_life}
        """)
    if user_life > computer_life:
        print(f'You win the game!')
    elif computer_life > user_life:
        print('Computer won the game')
    else:
        print('Game ended in a draw.')        



def get_random_number():
    random_number = random.randint(1, 3)
    return random_number


def get_user_input():
    options = ['rock', 'paper', 'scissors']
    user_input = input('Enter your weapon (rock, paper or scissors): ').strip().lower()

    while user_input not in options:
        try:
            user_input = input('Enter your weapon (rock, paper or scissors): ').strip().lower()
        except ValueError:
            continue
    return user_input



if __name__ == '__main__':
    print(main())