from utilities import *
from marvin_time import find_time
from logo import *
from options import *
from personality import *
from encrypter import *
from marvin_naughtscrosses import *

global CLOSE

def welcome():
    statements = ['\nHow can I help?', '\nWhat do you need me to do?', \
                  '\nWhat do you need?']
    print(statements[random.randint(0, 2)])


def console():
    '''asks how to help then redirects to other functions'''
    
    commands = [('thanks', thanks),
                ('thank', thanks),  
                ('time', find_time),
                ('calculator', calculator),
                ('calc', calculator),
                ('new cipher', new_cipher),
                ('options', options),
                ('settings', options),
                ('preferences', options),
                ('prefs', options),
                ('help', help),
                ('what can i do', help),
                ('man marvin', help),
                ('shit', curse_words),
                ('fuck', curse_words),
                ('goodbye', gift_shop),
                ('quit', gift_shop),
                ('close', gift_shop),
                ('see ya', gift_shop),
                ('how are you', personality),
                ('whats up', personality),
                ('how you doin', personality),
                ('gift shop', gift_shop),
                ('game', game),
                ('games', game),
                ('play', game),
                ('What can you do', help),
                ('what are you', help),
                ('what', help),
                ('clear', clear_w_logo),
                ('nevermind', okay)
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
    
    for string, command in commands:
        if string in query:
            commands[index][1]()
            understood = True
            break
        
        index += 1
            
    if understood == False:
        problem()


def gift_shop():
    print('\nSee you later Henry\n\n')
    clear()
    quit()


def main():
    clear()
    logo()
    while 4 == 4:
        console()
    
    clear()


main()