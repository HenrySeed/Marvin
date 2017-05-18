def calculator():
    '''type calculator and then you can enter equations to be answered'''
    equation = input('    Enter an equation:\n\n    > ')
    try:
        print('\n    = ' + str(eval(equation)))
    except:
        print('\n    Please enter a valid math equation\n')
        calculator()


commands = [('calculator', calculator),
            ('calc', calculator)]

help_options = [('calculator', 'Opens the calculator')]
