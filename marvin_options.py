import os.path

def display(prefs):
    print('')
    for keys,values in sorted(prefs.items()):
        print('    ' + keys + ': ' + values)
    print('')

def importer():
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'options.txt')    
    infile = open(filename, 'r')
    lines = infile.readlines() 
    lines = lines[4:]
    counter = 0
    for i in lines:
        if i.endswith('\n'):
            lines[counter] = i[0:-1]
        counter += 1
        
    prefs = {}
    for i in lines:
        i = i.split(':')
        prefs[i[0]] = i[1]
    return prefs

def change_name(prefs, header):
    name = input('\n    Enter name:\n    > ')
    prefs['name'] = name
    
    contents = ''
    for i in sorted(prefs.items()):
        contents += i[0] + ':' + i[1] + '\n'
    contents = header + contents
    
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'options.txt')    
    infile = open(filename, 'w')
    infile.write(contents)
    infile.close()
    

def change_location(prefs, header):
    location = input('\n    Enter location:\n    > ')
    prefs['location'] = location
    
    contents = ''
    for i in sorted(prefs.items()):
        contents += i[0] + ':' + i[1] + '\n'
    contents = header + contents
    
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'options.txt')    
    infile = open(filename, 'w')
    
    infile.write(contents)
    infile.close()
    
def leave():
    return 'okay'

def name():
    '''returns name'''
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'options.txt')    
    infile = open(filename, 'r')
    lines = infile.readlines()
    name = lines[5][5:]
    return name

def options(intro=False):
    prefs = importer()
    display(prefs)
    
    if intro == True:
        print('    To change a setting type change and then the name of the setting.\n')
    
    header = '# Preferences for mavin personal assistant (c) 2015\n\
# Designed by Henry Seed \n\
# Christchurch, New Zealand\n\
\n\
'
    
    query = input('    > ')
    query = query.lower()
    if query == 'change location':
        change_location(prefs, header)
        options()
    elif query == 'change name':
        change_name(prefs, header)
        options()
    elif query == 'help' or query == '?':
        print('\n    To change an option just type \'change\' and then the option name')
        print('    To quit just type \'quit\' or \'close\'\n') 
        options()
    elif query == 'exit' or query == 'close' or query == 'quit':
        leave()
    else:
        print('\n    To change an option just type \'change\' and then the option name')
        print('    To quit just type \'quit\' or \'close\'\n') 
        options()
