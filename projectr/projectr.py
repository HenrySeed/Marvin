import os

def get_proj_folder():
    '''asks for project folder if not exists'''

    return "~/Projects/"


def html():
    '''Makes a new html project'''

    name = input("Project Name: ")

    templates_dir = "~/dnm/marvin/projectr/templates/"

    projects_dir = get_proj_folder()

    os.system("mkdir " + projects_dir + name)
    os.system("mkdir " + projects_dir + name + "/static")
    os.system("mkdir " + projects_dir + name + "/static/css")
    os.system("mkdir " + projects_dir + name + "/static/js")
    os.system("mkdir " + projects_dir + name + "/static/images")

    os.system("cp " + templates_dir + "index.html " + projects_dir + name)
    os.system("touch " + projects_dir + name + "/static/css/stylesheet.css")