from subprocess import *

proj_dir = '~/Projects'

def new_proj():
    name = input("  Project Name > ")
    call(["mkdir", proj_dir + "/" + name])

def print_projs():
    ls = Popen("ls " + proj_dir, shell=True, stdout=PIPE).stdout.read().decode().split('\n')
    try:
        ls.remove('')
        ls.remove('archive')
    except:
        pass

    print('    Projects')

    for folder in ls[:-1]:
        print('        ├─ ' + folder)

    print('        └─ ' + ls[-1])


def setup():
    ls = Popen("ls " + proj_dir, shell=True, stdout=PIPE).stdout.read().decode().split('\n')
    try:
        ls.remove('')
        ls.remove('archive')
    except:
        pass

    for folder in ls:
        folder = folder.replace(' ', '\ ')
        contents = Popen("ls " + proj_dir + "/" + folder, shell=True, stdout=PIPE).stdout.read().decode().split('\n')
        if 'README' not in contents:
            print("{0:30}{1}".format(folder, "Fail"))
        else:
            print("{0:20}{1}".format(folder, "|o|"))
        print('---------------------')



commands = [("new_proj", new_proj),
            ("ls", setup)]

help_options = [("new_proj", "makes a new project in the defined project folder"),
                ("ls", "shows all the projects in the project directory")]
