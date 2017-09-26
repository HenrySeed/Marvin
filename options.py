import os.path

class Options():

    def __init__(self):
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'options.txt')
        lines = open(filename, 'r').read()
        lines = lines.split('\n')

        self.name, self.location = lines[0], lines[1]
        self.public_key = (int(lines[2].split(', ')[0]), int(lines[2].split(', ')[1]))
        self.private_key = (int(lines[3].split(', ')[0]), int(lines[3].split(', ')[1]))


    def save(self):
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'options.txt')
        infile = open(filename, 'w')

        output = self.name + '\n' + str(self.location) + '\n' + \
            str(self.public_key)[1:-1] + '\n' + str(self.private_key)[1:-1]

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
        self.name = input('Enter name: ')
        self.save()


    def change_cipher(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.save


    def change_location(self):
        self.location = input('Enter location: ')
        self.save()


def options(intro=False):
    print("    Options:")
    print('    To change a setting type change and then the name of the setting.')

    options = Options()
    print(options)


def change_option(string):
    options_obj = Options()
    string = string.lower()

    if string == 'location':
        options_obj.change_location()
    elif string == 'name':
        options_obj.change_name()
    else:
        print('    That option cant be changed, sorry.')

    print()
    options()
