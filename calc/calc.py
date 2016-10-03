def calculator():
    '''type calculator and then you can enter equations to be answered'''
    done = False
    while done == False:
        equation = input('CALC: (c) Henry Seed 2016 \n\
        Enter an equation or "q" to quit:\n\n    > ')

        try:
            print('\n    = ' + str(eval(equation)))
            done = True
        except:
            print('\n    Please enter a valid equation or "q" to quit.\n')
