import random
from marvin_naughtscrosses import *
import os
import sys
import logo
import subprocess

def calculator():
    '''type calculator and then you can enter equations to be answered'''
    equation = input('    Enter an equation:\n\n    > ')
    try:
        print('\n    = ' + str(eval(equation)))
    except:
        print('\n    Please enter a valid math equation\n')
        calculator()
    
    
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
    problem = ['Sorry I don\'t think i can do that.', 'What was that?', \
                'What do you need me to do again?', 'Sorry what was that?',\
                'I\'m sorry, Dave. I\'m afraid I can\'t do that.']  
    
    print('    Would you like to play Noughts and Crosses?')
    choice = input('\n    > ')
    
    if choice == 'yes' or choice == 'y':
        naughtscrosses()
        
    elif choice == 'no' or choice == 'n':
        print('\n    Well thats the only one I have at the moment, sorry')
        
    else:
        print()
        print('    ' + problem[random.randint(0, (len(problem)-1))])
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