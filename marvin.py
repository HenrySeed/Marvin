from options import *
from random import randint
import sys
import os
from logo import logo

from plugins import *


def help():
    help_options = [('options', 'Prints your current settings'),
                    ('help', 'Displays this message'),
                    ('quit', 'Quits marvin'),
                    ('clear', 'Clears the screen'),
                    ('plugins', 'Shows the currently loaded plugins')]

    for i in installed_plugins:
        help_options += (sys.modules['plugins.' + i].help_options)

    print('''    I\'m Marvin and I can help you with some simple tasks:

    Available Commands:
    ''')
    for i in help_options:
        print('        ' + i[0] + ':   ' + i[1])

    print('''
    Because I am designed for easy Human use, many commands will run on
    different other inputs as well so you always get what you want.''')


def problem():
    problem = ['Sorry I don\'t think i can do that.', 'What was that?',
    'What do you need me to do again?', 'Sorry what was that?',
    'I\'m sorry, Dave. I\'m afraid I can\'t do that.']

    print('    ' + problem[randint(0, (len(problem) - 1))])


def clear():
    if sys.stdin.isatty():
        os.system('clear')


def clear_w_logo():
    if sys.stdin.isatty():
        os.system('clear')
        logo()


def close():
    print('\n    See you later Henry\n\n')
    clear()
    quit()


def print_plugins():
    print('    Plugins installed in marvin/plugins:')
    for i in installed_plugins:
        print('     + ' + i)


def marvin():
    '''asks how to help then redirects to other functions'''

    commands = [('options', options),
                ('settings', options),
                ('preferences', options),
                ('prefs', options),
                ('help', help),
                ('what can i do', help),
                ('man marvin', help),
                ('goodbye', close),
                ('quit', close),
                ('q', close),
                ('close', close),
                ('see ya', close),
                ('clear', clear_w_logo),
                ('plugins', print_plugins)
                ]

    for i in installed_plugins:
        commands += (sys.modules['plugins.' + i].commands)

    query = input('\n> ')
    print()

    understood = False

    if 'encrypt' in query:
        encrypt(query)
        return None

    if 'decrypt' in query:
        decrypt(query)
        return None

    if 'change' in query:
        list_query = query.split(' ')
        change_option(list_query[1])
        return None

    for string, command in commands:
        if string in query:
            try:
                query = query.split(' ')
                command(query)
            except TypeError:
                command()

            understood = True
            break

    if understood == False:
        problem()


def main():
    clear()
    logo()
    while 4 == 4:
        marvin()
    clear()


main()
