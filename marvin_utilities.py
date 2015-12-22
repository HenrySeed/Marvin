import random

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
    
    
def help():
    print('I\'m Marvin and I can help you with some simple tasks: \n\n\
            Available Commands: \n\
            help/?:      Displays this message \n\
            time:        Displays the time \n\
            calculator:  Opens calculator for equations\n\
            options      Opens the options panel\n\
            close/quit   Quits Marvin')    
    
    

def curse_words():
    print('Look, I can see you\'re really upset about this. \n\
I honestly think you ought to sit down calmly, take a \n\
stress pill, and think things over.')    
    
def problem():
    problem = ['Sorry I don\'t think i can do that.', 'What was that?', \
                'What do you need me to do again?', 'Sorry what was that?',\
                'I\'m sorry, Dave. I\'m afraid I can\'t do that.']    
    
    print(problem[random.randint(0, (len(problem)-1))])