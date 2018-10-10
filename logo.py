from random import randint
from colors import colors, crayon

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
    quote = "Throws errors so you don\'t have to."
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

    color_logo = '''
{1} __________________________________________________________________________
{1}|                                                                          |
{1}|  ****   ****      ****    *********  ***    *** *********** ****    ***  |
{1}|  *###***####*    *####*   *##    *## *##    *##     *##     *####   *##  |
{1}|  *## *#### *##  *##  *##  *##    *## *##    *##     *##     *#####  *##  |
{1}|  *##  *##  *## *##****### *##****##  *##    *##     *##     *###### *##  |
{1}|  *##       *## *##    *## *##    *##  *##  *##      *##     *## ###*###  |
{1}|  *##       *## *##    *## *##    *##   *#**##       *##     *##   #####  |
{1}|  *##       *## *##    *## *##    *##    *###    ****###**** *##    ####  |
{1}|__________________________________________________________________________|
{1}                                           |                         |
{1}   {0:37}   |       Version {2:4}      |
{1}                                           |_________________________|
    '''.format(quote, spacer, version)

    colorsList = [
        ("Red", colors.bg_red, colors.bg_red_bright),
        ("Yellow", colors.bg_yellow, colors.bg_yellow_bright),
        ("Green", colors.bg_green, colors.bg_green_bright),
        ("Cyan", colors.bg_cyan, colors.bg_cyan_bright),
        ("Blue", colors.bg_blue, colors.bg_blue_bright),
        ("Indigo", colors.bg_indigo, colors.bg_indigo_bright)
    ]

    formattedLogo = ''
    count = -2
    for line in color_logo.split('\n'):
        if count < 8:
            color = colorsList[int(count / 2)]
            line = line.replace('#', crayon(' ', color[1]))
            line = line.replace('*', crayon(' ', color[2])) 
            count += 1
        formattedLogo += line + "\n"
    
    
    print('{0:>200}'.format(formattedLogo))


    
