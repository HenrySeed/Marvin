from random import randint
from terminal_info import terminal_info

def logo():
    
    quotes = ["Throws errors so you don\'t have to.", "Functional Killer Robot",\
              "Sweet talkin woman", "Hard work'n man", "Scandelously self-consumed", \
              "Generally a nice guy", "Sometimes cares", "Gets angry at melancholy doors",
              "Not overly content, for a robot", "Witty, for a robot", \
              "Running for president", "Marvin for presidant 2016!", "Version 2 !!!"]
    
    for i in quotes:
        quotes[quotes.index(i)] = "{0:37}".format("\"" + i + "\"")
    
    quote = quotes[randint(0, len(quotes)-1)]
    
    width, height = terminal_info.getTerminalSize()
    
    spacer = (width - 77)//2 * ' '
    
    logo = '''
{1} __________________________________________________________________________
{1}|                                                                          |
{1}|  ####   ####      ####    #########  ###    ### ########### ####    ###  |
{1}|  ############    ######   ###    ### ###    ###     ###     #####   ###  |
{1}|  ### ##### ###  ###  ###  ###    ### ###    ###     ###     ######  ###  |
{1}|  ###  ###  ### ########## #########  ###    ###     ###     ####### ###  |
{1}|  ###       ### ###    ### ###    ###  ###  ###      ###     ### #######  |
{1}|  ###       ### ###    ### ###    ###   ######       ###     ###   #####  |
{1}|  ###       ### ###    ### ###    ###    ####    ########### ###    ####  |
{1}|__________________________________________________________________________|
{1}                                           |                         |       
{1}   {0:37}   |       Version 2.01      |       
{1}                                           |_________________________|       
    '''.format(quote, spacer)
    
    print('{0:>200}'.format(logo))
