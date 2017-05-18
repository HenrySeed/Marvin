from random import randint
import os
import sys
from logo import logo


def clear_w_logo():
    if sys.stdin.isatty():
        os.system('clear')
        logo()

def all_games():
    installed_games = []
    for name in os.listdir("plugins/games"):
        if name not in ['__init__.py', '.DS_Store']:
             name = name.replace('_', ' ')
             name = name.title()
             if 'And' in name: name = name.replace('And', 'and')
             if 'Or' in name: name = name.replace('Or', 'or')
             installed_games.append(name)

    return installed_games

def game():
    installed_games = all_games()

    print('    Games installed in marvin/plugins/games:')
    print('    To play, type "play noughts and crosses" or just "play 1"\n')

    for i in range(1, len(installed_games)+1):
        print('     {0}) {1}'.format(i, installed_games[i-1]))


def play_game(query):
    installed_games = all_games()
    query.remove('play')

    try:
        query = int(query[0])
        if query <= len(installed_games) and query > 0:
            query -= 1

            game = installed_games[query]
            game = game.replace(' ', '_')
            game = game.lower()

            if sys.stdin.isatty():
                os.system('clear')
            os.system('python3 plugins/games/' + game + '/main.py')
            clear_w_logo()

        else:
            print('I don\'t seem to ha ve that game sorry')

    except:

        for game in installed_games:
            game = game.replace(' ', '_')
            game = game.lower()

            guess1 = '_'.join(query)
            guesses = [guess1]

            if game in guesses:
                if sys.stdin.isatty():
                    os.system('clear')
                os.system('python3 plugins/games/' + game + '/main.py')
                clear_w_logo()
            else:
                print('I don\'t seem to have that game sorry')


commands = [('game', game),
            ('games', game),
            ('play', play_game),]

help_options = [('game', 'Shows what games we can play')]
