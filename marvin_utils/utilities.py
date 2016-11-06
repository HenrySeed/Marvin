import random
import os
import sys
import subprocess


from marvin_utils import logo
from naughts_crosses import naughts_crosses
    
def thanks():
    print('It\'s all good')
    
def okay():
    print('Okay man whatever you want.')
    
    
def help():
    print('''I\'m Marvin and I can help you with some simple tasks:
    
            Available Commands: 
            
            help/?:            Displays this message 
            time:              Displays the time 
            calculator:        Opens calculator for equations
            options            Opens the options panel
            close/quit         Quits Marvin
            encrypt [message]  Emcrypts a message using your saved cipher
            new cipher         Builds a new RSA cipher and can save it
            
        Because I am designed for easy Human use, many commands will run on 
        different other inputs as well so you always get what you want.''')    
    
    
def curse_words():
    print('Look, I can see you\'re really upset about this. \n\
I honestly think you ought to sit down calmly, take a \n\
stress pill, and think things over.')   

    
def problem():
    problem = ['Sorry I don\'t think i can do that.', 'What was that?', \
                'What do you need me to do again?', 'Sorry what was that?',\
                'I\'m sorry, Dave. I\'m afraid I can\'t do that.']    
    
    print(problem[random.randint(0, (len(problem)-1))])
    
    
def game():
    
    print('    (1) Noughts and Crosses. A classic kids game')
    choice = input('\n    > ')
    
    if '1' in choice:
        naughts_crosses.naughtscrosses()

        
    elif choice == 'close' or choice == 'q':
        print('\n    Well these are the only ones I have at the moment, sorry')
        
    else:
        print()
        print('    ' + problem())
        print()
        game()
        
        
def clear():
    if sys.stdin.isatty():
        os.system('clear')
        
def clear_w_logo():
    if sys.stdin.isatty():
        os.system('clear')
        logo.logo()
        
def ip():
    proc = subprocess.Popen(['dig +short myip.opendns.com @resolver1.opendns.com'], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    print('Your current ip is ' + str(out)[2:-3])