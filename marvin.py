from marvin_utils import utilities
from marvin_utils import logo
from marvin_utils import encrypter
from marvin_utils import options
from marvin_utils import personality

from projectr import projectr
from terminal_info import *
from naughts_crosses import *
from cute_time import cute_time
from calc import calc


global CLOSE

def welcome():
    statements = ['\nHow can I help?', '\nWhat do you need me to do?', \
                  '\nWhat do you need?']
    print(statements[random.randint(0, 2)])


def console():
    '''asks how to help then redirects to other functions'''
    
    commands = [('thanks', utilities.thanks),
                ('thank', utilities.thanks),  
                ('time', cute_time.find_time),
                ('calculator', calc.calculator),
                ('calc', calc.calculator),
                ('new cipher', encrypter.new_cipher),
                ('options', options.options),
                ('settings', options.options),
                ('preferences', options.options),
                ('prefs', options.options),
                ('help', utilities.help),
                ('what can i do', utilities.help),
                ('man marvin', utilities.help),
                ('shit', utilities.curse_words),
                ('fuck', utilities.curse_words),
                ('goodbye', gift_shop),
                ('quit', gift_shop),
                ('close', gift_shop),
                ('see ya', gift_shop),
                ('how are you', personality.personality),
                ('whats up', personality.personality),
                ('how you doin', personality.personality),
                ('gift shop', gift_shop),
                ('game', utilities.game),
                ('games', utilities.game),
                ('play', utilities.game),
                ('What can you do', utilities.help),
                ('what are you', utilities.help),
                ('what', utilities.help),
                ('clear', utilities.clear_w_logo),
                ('nevermind', utilities.okay),
                ('ip', utilities.ip)
                ]

    query = input('\n> ')
    print()
    
    understood = False
    index = 0
    
    if 'encrypt' in query:
        encrypt(query)
        return None
        
    if 'decrypt' in query:
        decrypt(query)
        return None

    if ('new' in query or 'project' in query) and 'html' in query:
        projectr.html()
        return None
    
    if query == 'q':
        gift_shop()
        return None

    for string, command in commands:
        if string in query:
            commands[index][1]()
            understood = True
            break
        
        index += 1
            
    if understood == False:
        utilities.problem()


def gift_shop():
    print('\nSee you later Henry\n\n')
    utilities.clear()
    quit()


def main():
    utilities.clear()
    logo.logo()
    while 4 == 4:
        console()
    
    utilities.clear()


main()