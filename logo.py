from random import randint

def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])

def logo():

    version = '1.0'

    quotes = ["Throws errors so you don\'t have to.", "Functional Killer Robot",\
              "Sweet talkin woman", "Hard work'n man", "Scandelously self-consumed", \
              "Generally a nice guy", "Sometimes cares", "Gets angry at melancholy doors",
              "Not overly content, for a robot", "Witty, for a robot", \
              "Running for president", "Marvin for president 2016!", "Version 2 !!!"]

    for i in quotes:
        quotes[quotes.index(i)] = "{0:37}".format("\"" + i + "\"")

    quote = quotes[randint(0, len(quotes)-1)]

    width, height = getTerminalSize()

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
{1}   {0:37}   |       Version {2:4}      |
{1}                                           |_________________________|
    '''.format(quote, spacer, version)

    print('{0:>200}'.format(logo))
