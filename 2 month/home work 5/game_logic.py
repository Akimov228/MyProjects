from random import choice
from decouple import config

def game_casino():
    bank = int(config('MY_MONEY'))
    while True:
        random_slot = choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,2,6,27,28,29,30])
        print(random_slot)
        user = input('Do u wanna play? ')
        if user == 'y':
            choose_slot = input('Choose the slot number: ')
            bet_money = int(input('Your bet: '))
            if choose_slot != str(random_slot) and bet_money <= bank:
                bank -= int(bet_money)
                print(f'You lost -{bet_money}$ ')
            elif choose_slot == str(random_slot) and bet_money <= bank:
                bank += int(bet_money) * 2
                print(f'You won +{int(bet_money) * 2}$ ')

        elif user == 'n':
                print(f'Your capital is: {bank}')
                break

