import random
import sys

game_characters = {'p': 'paper', 'r': 'rock', 's': 'scissors'}
output = 0
points = [0, 0, 0]
wins, loss, draws = points
print('ROCK, PAPER, SCISSORS')
print('Enter Your Move: (r)ock (p)aper (s)cissors (q)uit')
try:
    while True:
        move = (input('Input Your Move Here// ')).lower()
        if move == 'q':
            sys.exit()
            # paper
        elif move == 'p':
            move_get = game_characters.get('p', 'none')
            print('')
            print(f'{move_get} versus...')
            random_game_character = random.choice(list(game_characters.values()))
            print(random_game_character)
            if move_get == random_game_character:
                print(''' 
    Result: it is a tie
     ''')
                draws += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')
            elif random_game_character == game_characters['r']:
                print('''
    Result: You Won!
     ''')
                wins += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')
            else:
                print('''  
    you lose!, scissors cuts paper
     ''')
                loss += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')

                # rock
        elif move == 'r':
            move_get = game_characters.get('r', 'none')
            print(' ')
            print(f'{move_get} versus...')
            random_game_character = random.choice(list(game_characters.values()))
            print(random_game_character)
            if move_get == random_game_character:
                print(''' 
it is a tie
 ''')
                draws += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')
            elif random_game_character == game_characters['s']:
                print(''' 
You Won!
 ''')
                wins += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')
            else:
                print(''' 
you lose!, paper covers rock
 ''')
                loss += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')

                # scissors
        elif move == 's':
            move_get = game_characters.get('s', 'none')
            print(' ')
            print(f'{move_get} versus...')
            random_game_character = random.choice(list(game_characters.values()))
            print(random_game_character)
            if move_get == random_game_character:
                print(''' 
    it is a tie
     ''')
                draws += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')
            elif random_game_character == game_characters['p']:
                print(''' 
    You Won!
     ''')
                wins += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')
            else:
                print(''' 
    you lose, rock smashes scissors!
     ''')
                loss += 1
                print(f'wins:{wins}, draws:{draws}, loss:{loss}')
        else:
            print('Letter Not Recognized')
            print('Try Typing: r, p, s, q')
            print(' ')
            continue
except KeyboardInterrupt:
    print('error: keyboard interrupt')
