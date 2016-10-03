def calculator():
    '''type calculator and then you can enter equations to be answered'''
    done = False
    print('CALC: (c) Henry Seed 2016 \n\
      Enter an equation or "q" to quit:')
    while done == False:
        equation = input('\nCALC: > ')

        if equation == 'q':
            done = True
        else:
            try:
                print('      = ' + str(eval(equation)))
            except:
                print('\n      Please enter a valid equation or "q" to quit.')
