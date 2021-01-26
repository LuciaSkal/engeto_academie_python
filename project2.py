import random

def game():
    print('*' * 90)
    print('''
    Welcome, to the COWS and BULLS game.
    I have chosen number from 0 to 9 arranged in a random order.
    You need to input a 4 digit number as a guess at what I have chosen.
    Let's play...
    ''')
    print('*' * 90)
    cislo = tajny_cislo(4)
    # print(f'tajny cislo {cislo}')
    pocet_hadani = 0
    while True:
        tip = input('\nEnter your guess: ')
        pocet_hadani += 1
        print('-' * 30)
        if nespravny_tip(tip):
            continue

        bulls, cows = bulls_and_cows(tip, cislo)

        if status_hry(bulls, cows, pocet_hadani):
            break
        print('-' * 30)

def tajny_cislo(delka):
    nahodny_cislo = ''
    while len(nahodny_cislo) < delka:
        nove = str(random.randint(0, 9))
        if nove not in nahodny_cislo:
            nahodny_cislo += nove
    return nahodny_cislo

def nespravny_tip(vstup):
    result = False

    if not vstup.isdecimal() or len(vstup) != 4:
        print('\n>>>Enter whole 4-digit number!<<<')
        result = True

    if len(set(vstup)) != len(vstup):
        print('\n>>>Enter a number not repeating the digits!<<<')
        result = True

    return result

def bulls_and_cows(vstup, vyber_cislo):
    bulls = 0
    cows = 0
    for i, csl in enumerate(vstup):
        if csl == vyber_cislo[i]:
            bulls += 1
        elif csl in vyber_cislo:
            cows += 1
    return bulls, cows

def status_hry(bulls, cows, pocet_hadani):
    game_over = False

    if bulls == 4:
        print('*' * 40,
            f'Game Over ---> found it after {pocet_hadani} guesses',
            '*' * 40,
            sep='\n'
        )
        game_over = True
    else:
        print(f'{bulls} bulls | {cows} cows | {pocet_hadani} guesses')

    return game_over

game()