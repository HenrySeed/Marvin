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
    
    spacer_wide = (width - 77)//2 * ' '
    
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
{1}   {0:37}   |       Version 2.03      |       
{1}                                           |_________________________|       
    '''.format(quote, spacer_wide)


    spacer_narrow = (width - 50)//2 * ' '
    logo_small = '''
{0} _______________________________________________ 
{0}|                                               |
{0}|  ##   ##   ##   ###### #    # ####### #    #  |
{0}|  ### ###  #  #  #    # #    #    #    ##   #  |
{0}|  # ### #  ####  #####  #    #    #    # ## #  |
{0}|  #  #  # #    # #    #  #  #     #    #   ##  |
{0}|  #     # #    # #    #   #    ####### #    #  |
{0}|_______________________________________________|
{0}                   |                         |
{0}                   |       Version 2.03      |
{0}                   |_________________________|   
'''.format(spacer_narrow)
    

    if width < 78:
        print(logo_small)
    else:
        print('{0:>200}'.format(logo))
