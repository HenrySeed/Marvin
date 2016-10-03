import os.path

class Options():
    
    def __init__(self):
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'options.txt')    
        infile = open(filename, 'r').read()
        
        line = infile.split(',')
        
        self.name, self.location = line[0], line[1]
        self.public_key = (int(line[2][1:]),int(line[3][1:-1]))
        self.private_key = (int(line[4][1:]),int(line[5][1:-1]))

    
    def save(self):
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'options.txt')    
        infile = open(filename, 'w')
        
        output = self.name + ',' + str(self.location) + ',' + \
            str(self.public_key) + ',' + str(self.private_key)
            
        infile.write(output)
        infile.close()        
        
            
    def __str__(self):
        return """
        Name:       {0}
        Location:   {1}
        Public key  {2}
        Private Key {3}
        """.format(self.name, self.location, self.public_key, self.private_key)


    def change_name(self):
        self.name = input('\n    Enter name:\n    > ')
        self.save()
        
        
    def change_cipher(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.save
    

    def change_location(self):
        self.location = input('\n    Enter location:\n    > ')
        self.save()


def options(intro=False):
    
    if intro == True:
        print('    To change a setting type change and then the name of the setting.\n')
        
    quit = False
    
    while quit == False:
        
        options = Options()
        print(options)
        
        query = input('    > ').lower()
        
        if query == 'exit' or query == 'close' or query == 'quit': quit = True 
        
        elif query == 'change location': options.change_location()
        
        elif query == 'change name': options.change_name()
        
        else:
            print('\n    To change an option just type \'change\' and then the option name')
            print('    To quit just type \'quit\' or \'close\'\n') 
