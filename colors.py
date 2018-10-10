
class colors:
    fg_dim = '\033[2m'
    fg_bold = '\033[1m'
    fg_underline = '\033[3m'

    fg_black = '\033[30m'
    fg_red = '\033[31m'
    fg_green = '\033[32m'
    fg_yellow = '\033[33m'
    fg_blue = '\033[34m'
    fg_indigo = '\033[35m'
    fg_cyan = '\033[36m'
    fg_white = '\033[97m'

    fg_black_bright = '\033[90m'
    fg_red_bright = '\033[91m'
    fg_green_bright = '\033[92m'
    fg_yellow_bright = '\033[93m'
    fg_blue_bright = '\033[94m'
    fg_indigo_bright = '\033[95m'
    fg_cyan_bright = '\033[96m'

    bg_black = '\033[40m'
    bg_red = '\033[41m'
    bg_green = '\033[42m'
    bg_yellow = '\033[43m'
    bg_blue = '\033[44m'
    bg_indigo = '\033[45m'
    bg_cyan = '\033[46m'

    bg_black_bright = '\033[100m'
    bg_red_bright = '\033[101m'
    bg_green_bright = '\033[102m'
    bg_yellow_bright = '\033[103m'
    bg_blue_bright = '\033[104m'
    bg_indigo_bright = '\033[105m'
    bg_cyan_bright = '\033[106m'

    reset = '\033[0m'


def crayon(string, fg='\033[30m', bg='\033[30m'):
    return fg + bg + string + colors.reset


