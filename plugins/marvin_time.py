import datetime

def find_time():
    '''finds amd then returns time in 12 hr format hh:mm'''
    hour = int(datetime.datetime.strftime(datetime.datetime.now(), '%H'))
    minutes = datetime.datetime.strftime(datetime.datetime.now(), '%M')

    if minutes == '0':
        minutes == '00'

    if hour < 3:
        print('\n    Even for you its pretty late.')

    elif hour > 3 and hour < 7:
        print('\n    Its pretty early.')

    if hour == 00:
        print('    It\'s 12' + ':' + str(minutes) + ' in the morning')

    elif hour == 12:
        print('    It\'s 12' + ':' + str(minutes) + ' in the afternoon')

    elif 13 <= hour and hour < 17:
        print('    It\'s ' + str(hour - 12) + ':' + str(minutes) + ' in the afternoon')

    elif 17 <= hour and hour < 20:
        print('    It\'s ' + str(hour - 12) + ':' + str(minutes) + ' in the evening')

    elif 20 <= hour and hour < 24:
        print('    It\'s ' + str(hour - 12) + ':' + str(minutes) + ' at night')

    else:
        print('    It\'s ' + str(hour) + ':' + str(minutes) + ' in the morning')

commands = [('time', find_time)]
help_options = [('time', 'Shows the current time')]
