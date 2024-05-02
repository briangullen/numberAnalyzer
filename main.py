player_name = input('What is your name? ')
play_again = 'yes'
while True:
    if play_again == 'yes':
        chosen_number = int(input(f'Hello {player_name} Enter a number between 1 and 100: '))
        print(f'Ok {player_name} you have chosen {chosen_number}')
        if chosen_number % 2 == 0:
            if 2 <= chosen_number <= 24:
                print(f'{chosen_number} is Even and less than 25')
            elif 26 <= chosen_number <= 60:
                print(f'{chosen_number} is Even and between 26 and 60 inclusive')
            else:
                print(f'{chosen_number} is Even and greater than 60')
        else:
            if chosen_number < 60:
                print(f'{chosen_number} is Odd and less than 60')
            else:
                print(f'{chosen_number} is Odd and more than 60')
        play_again = input(f'Would you like to play again {player_name}? Please enter "yes" or "no": ')
    else:
        print(f'Thanks for playing {player_name}!')
        break
