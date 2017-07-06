# Taro-Color
python color print

```from colors import colors```

usage:

```colors.color(msg, foreground = None, background = None, format_str=None)```:

```foreground``` and ```background``` color could use one of {'BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE', 'default, 'BRIGHT_RED', 'BRIGHT_GREEN', 'BRIGHT_YELLOW' , 'BRIGHT_BLUE' , 'BRIGHT_MAGENTA', 'BRIGHT_CYAN'}

```format_str```: 'b' for bold, 'i' for italic, 'u' for underline

```colors.rgb_color(msg, foreground = (r,g,b), background = (r, g, b), format_str=None)```:
```r```, ```g```, ```b``` should be ```int``` of ```0...255```.
