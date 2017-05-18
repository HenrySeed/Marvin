import os

'''
This just adds all plugins in the plugins folder to a central module
most of the code is just nicked from stack overflow duh.
'''

installed_plugins = []

dir_path = os.path.dirname(os.path.realpath(__file__))

for name in os.listdir(dir_path):
    if name.endswith(".py") and name != '__init__.py':
          #strip the extension
         module = name[:-3]
         # set the module name in the current global name space:
         __import__("plugins." + module)
         installed_plugins.append(module)
