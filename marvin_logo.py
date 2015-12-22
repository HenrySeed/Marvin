from random import randint

def logo():
    
    quotes = ["Throws errors so you don\'t have to.", "Functional Killer Robot",\
              "Sweet talkin woman", "Hard work'n man", "Scandelously self-consumed", \
              "Generally a nice guy", "Sometimes cares", "Gets angry at melancholy doors",
              "Not overly content, for a robot", "Witty, for a robot", \
              "Running for president", "Marvin for presidant 2016!", "Version 2 !!!"]
    
    for i in quotes:
        quotes[quotes.index(i)] = "{0:37}".format("\"" + i + "\"")
    
    quote = quotes[randint(0, len(quotes)-1)]
    
    logo = '\
                \n\
     __________________________________________________________________________\n\
    |                                                                          |\n\
    |  ####   ####      ####    #########  ###    ### ########### ####    ###  |\n\
    |  ############    ######   ###    ### ###    ###     ###     #####   ###  |\n\
    |  ### ##### ###  ###  ###  ###    ### ###    ###     ###     ######  ###  |\n\
    |  ###  ###  ### ########## #########  ###    ###     ###     ####### ###  |\n\
    |  ###       ### ###    ### ###    ###  ###  ###      ###     ### #######  |\n\
    |  ###       ### ###    ### ###    ###   ######       ###     ###   #####  |\n\
    |  ###       ### ###    ### ###    ###    ####    ########### ###    ####  |\n\
    |__________________________________________________________________________|\n\
                                               |                         |       \n\
       {0:37}   |       Version 2.01      |       \n\
                                               |_________________________|       \n\
                                               '.format(quote)
    
    print('{0:>200}'.format(logo))
