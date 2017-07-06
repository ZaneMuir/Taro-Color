class colors:
    COLOR = {'BLACK' : '\033[30m',
    'RED' : '\033[31m',
    'GREEN' : '\033[32m',
    'YELLOW' : '\033[33m',
    'BLUE' : '\033[34m',
    'MAGENTA' : '\033[35m',
    'CYAN' : '\033[36m',
    'WHITE' : '\033[37m',
    'BRIGHT_RED' : '\033[91m',
    'BRIGHT_GREEN' : '\033[92m',
    'BRIGHT_YELLOW' : '\033[93m',
    'BRIGHT_BLUE' : '\033[94m',
    'BRIGHT_MAGENTA' : '\033[95m',
    'BRIGHT_CYAN' : '\033[96m'}


    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'

    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'

    ENDC = '\033[0m'

    @staticmethod
    def bold(msg):
        return colors.BOLD+msg+colors.ENDC

    @staticmethod
    def italic(msg):
        return colors.ITALIC+msg+colors.ENDC

    @staticmethod
    def underline(msg):
        return colors.UNDERLINE+msg+colors.ENDC

    @staticmethod
    def color(msg, colorname):
        return colors.COLOR[colorname] + msg+ colors.ENDC

if __name__ == '__main__':
    print(colors.bold(colors.color('hi','GREEN')))
