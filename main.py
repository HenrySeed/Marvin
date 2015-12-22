from marvin_utilities import *
from marvin_time import *
from marvin_logo import *
from marvin_options import *
from marvin_personality import *

global CLOSE

def welcome():
    statements = ['\nHow can I help?', '\nWhat do you need me to do?', \
                  '\nWhat do you need?']
    print(statements[random.randint(0, 2)])


def console():
    '''asks how to help then redirects to other functions'''
    
    commands = {'whats the time?': find_time,
                'time': find_time,
                'calculator': calculator,
                'calc': calculator,
                'thanks': thanks,
                'thankyou': thanks,
                'options': options,
                'settings': options,
                'preferences': options,
                'prefs': options,
                'help': help,
                'what can i do': help,
                'man marvin': help,
                'shit': curse_words,
                'fuck': curse_words,
                'goodbye': leave,
                'quit': leave,
                'close': leave,
                'see ya': leave,
                'how are you': personality,
                'whats up': personality,
                'how you doin': personality,
                '?': help,
                'gift shop': gift_shop,
                '`': gift_shop,
                }
    
    query = input('\n> ')
    print()
    understood = False
    for i in commands.keys():
        if i in query:
            commands[i]()
            understood = True
            break
            
    if understood == False:
        problem()

def gift_shop():
    sure = input('Are you sure?\n\n> ')
    if 'yes' in sure or 'y' in sure:
        print('\nExiting through the giftshop...\n\n')
        quit()
    else:
        return None
    
def main():
    logo()
    while 4 == 4:
        console()


main()