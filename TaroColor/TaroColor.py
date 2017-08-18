import re
from color import xkcd_color
def hex2rgb(hex_str):
    r, g, b = re.findall(r'\#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})', hex_str)[0]
    result = (int('0x%s'%r, base=16), int('0x%s'%g, base=16), int('0x%s'%b, base=16))
    print(result)
    return result

class TaroColor:
    COLOR = {'BLACK' : 0,
    'RED' : 1,
    'GREEN' : 2,
    'YELLOW' : 3,
    'BLUE' : 4,
    'MAGENTA' : 5,
    'CYAN' : 6,
    'WHITE' : 7,
    'default': 9,
    'BRIGHT_RED' : 61,
    'BRIGHT_GREEN' : 62,
    'BRIGHT_YELLOW' : 63,
    'BRIGHT_BLUE' : 64,
    'BRIGHT_MAGENTA' : 65,
    'BRIGHT_CYAN' : 66}

    foreground = 30
    background = 40

    BOLD = '\033[1m'   #b
    ITALIC = '\033[3m'              #i
    UNDERLINE = '\033[4m'           #u

    ENDC = '\033[0m'

    @staticmethod
    def color(msg, foreground = None, background = None, format_str=None):
        '''TaroColor.color(msg, foreground = None, background = None, format_str=None)

        foreground and background color could use one of
        {\'BLACK\', \'RED\', \'GREEN\', \'YELLOW\', \'BLUE\', \'MAGENTA\', \'CYAN\', \'WHITE\', \'default, \'BRIGHT_RED\', \'BRIGHT_GREEN\', \'BRIGHT_YELLOW\' , \'BRIGHT_BLUE\' , \'BRIGHT_MAGENTA\', \'BRIGHT_CYAN\'}

        format_str: \'b\' for bold, \'i\' for italic, \'u\' for underline
        '''

        prefix = '\033[%d;%dm'
        target_foreground = foreground or 'default'
        target_background = background or 'default'

        if format_str:
            prefix = '\033[%s;%s;%sm'
            _format = []
            for i in format_str:
                if i == 'b':
                    _format.append('1')
                elif i == 'i':
                    _format.append('3')
                elif i == 'u':
                    _format.append('4')
            return prefix%(';'.join(_format), TaroColor.COLOR[target_background]+TaroColor.background, TaroColor.COLOR[target_foreground]+TaroColor.foreground) + msg + TaroColor.ENDC


        return prefix%(TaroColor.COLOR[target_background]+TaroColor.background, TaroColor.COLOR[target_foreground]+TaroColor.foreground) + msg + TaroColor.ENDC

    @staticmethod
    def rgb_color(msg, foreground = None, background = None, format_str=None):
        '''TaroColor.rgb_color(msg, foreground = (r,g,b), background = (r, g, b), format_str=None)
        r, g, b should be int of 0...255.

        foreground and background color could use one of
        {\'BLACK\', \'RED\', \'GREEN\', \'YELLOW\', \'BLUE\', \'MAGENTA\', \'CYAN\', \'WHITE\', \'default, \'BRIGHT_RED\', \'BRIGHT_GREEN\', \'BRIGHT_YELLOW\' , \'BRIGHT_BLUE\' , \'BRIGHT_MAGENTA\', \'BRIGHT_CYAN\'}

        format_str: \'b\' for bold, \'i\' for italic, \'u\' for underline
        '''

        prefix = '\033[%s;%sm'
        if foreground:
            target_foreground = '38;2;%d;%d;%d'%foreground
        else:
            target_foreground = '39'
        if background:
            target_background = '48;2;%d;%d;%d'%background
        else:
            target_background = '49'

        if format_str:
            prefix = '\033[%s;%s;%sm'
            _format = []
            for i in format_str:
                if i == 'b':
                    _format.append('1')
                elif i == 'i':
                    _format.append('3')
                elif i == 'u':
                    _format.append('4')
            return prefix%(';'.join(_format), target_foreground,target_background) + msg + TaroColor.ENDC

        return prefix%(target_foreground,target_background) + msg + TaroColor.ENDC

    @staticmethod
    def xkcd_color(msg, foreground_name=None, background_name=None, format_str=None):
        if foreground_name in xkcd_color.keys():
            foreground = hex2rgb(xkcd_color[foreground_name])
        else:
            foreground = None
        if background_name in xkcd_color.keys():
            background = hex2rgb(xkcd_color[background_name])
        else:
            background = None

        return TaroColor.rgb_color(msg, foreground=foreground, background=background, format_str=format_str)

if __name__ == '__main__':
    print(TaroColor.xkcd_color('hi',None,'bruise', 'biu'))
