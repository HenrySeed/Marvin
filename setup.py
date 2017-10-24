#!/usr/bin/python

import sys
import os

def getTerminalSize():
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
    return int(cr[1]), int(cr[0])


def clear():
    if sys.stdin.isatty():
        os.system('clear')


def install(pad_x):
    location = '~/marvin'
    print(pad_x + 'The current install directory is set to ' + location)
    prompt = input(pad_x + 'Is this correct? (Y/N): ').lower()

    if prompt == 'y':
        pass
    else:
        location = input(pad_x + 'New install location: ')

    print('\n' + pad_x + 'Cool, so marvin will be installed to {}'.format(location))
    prompt = input(pad_x + 'The install will take 2MB of space continue (Y/N): ').lower()

    if prompt == 'y':

        print('\n' + pad_x + "Installing...\n")
        return 0
    else:
        print('\n' + pad_x + "exiting...\n")
        return 0


def setup():
    logo = ["  o              .                              o                 .          o               .                 o                         .            .               o                         o         ",
    "                                             .                                                                                    o                                                         .    .        ",
    "   o                                                               .                                  .                                                                                                   ",
    "                              .    \\\  .                        __________________________________________________________________________                                                                ",
    "                 o                  \\\                 o       |                                                                          | o               o             .               .          .    ",
    "      .                              \\\_____                   |  ####   ####      ####    #########  ###    ### ########### ####    ###  |                                                               ",
    "                            .       / \\\    \                . |  ############    ######   ###    ### ###    ###     ###     #####   ###  |                                                               ",
    "                                   /   \\\    \                 |  ### ##### ###  ###  ###  ###    ### ###    ###     ###     ######  ###  |          .                             .            o         ",
    "         o                        |     \\\    |     .          |  ###  ###  ### ########## #########  ###    ###     ###     ####### ###  | .                   .         .                               ",
    "                     o             \     \\\  /                 |  ###       ### ###    ### ###    ###  ###  ###      ###     ### #######  |                                                               ",
    "                                 .  \_____\\\/                  |  ###       ### ###    ### ###    ###   ######       ###     ###   #####  |                                        .                      ",
    "              .                            \\\ .              o |  ###       ### ###    ### ###    ###    ####    ########### ###    ####  |             o                                         .       ",
    "                                            \\\                 |__________________________________________________________________________|                                            o                  ",
    "                                                                                                                             o                                       o                                    ",
    "                            o                       o                          .                               .                                   .                                                      ",
    "       .                             .                               .                                                       ____                                                                       . ",
    "                  o                                                                                   .                     /    \                                               .                        ",
    "                                             .            .                |            o                                 ==========       o                                                              ",
    "                                                                           |                                                \____/                        .                                   o           ",
    "                    .                                            .       --+--                                                                                           .                                ",
    "                                   .                                    o  |                                                                                                                          .   ",
    "      o                                             o                      |                                                                    .            .                    .                       ",
    "                                                                                      o                      .                                                                                  o         ",
    "                   o           o                                                                                                     o                                                                    ",
    "     .                                         .                o                                        .                      .                        o               o                                ",
    "                                                                                                                                                                                                     .   ."]

    width = getTerminalSize()[0]
    string_start = int(len(logo[0])/2 - (width/2))

    # print(string_start, string_start+width)
    # print(width, len(logo[0]))

    if width > len(logo[0]):
        padding_x = int(width/2 - len(logo[0])/2) * ' '
        for i in logo:
            print(padding_x + i)
    else:
        for i in logo:
            print(i[string_start:string_start+width])

    pad_x = int(width/2 - 40) * ' '

    print(pad_x + '\"Smarmiest personal assistant in the whole galaxy\"')
    prompt = input(pad_x + "Do you wish to start the install? (Y/N): ").lower()
    print()

    if prompt == "y":
        install(pad_x)
    else:
        print(pad_x + "exiting...\n")
        return 0



clear()

setup()
