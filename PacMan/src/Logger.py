import pygame

class Style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BG_RED = '\33[41m'
    BG_BLUE   = '\33[44m'
    BG_VIOLET = '\33[45m'
    UNDERLINE = '\033[4m'
    BOLD = '\33[1m'
    RESET = '\033[0m'

def info(output):
    start = Style.BOLD + Style.GREEN + "Info:" + Style.RESET + " "
    if isinstance(output, str):
        print(start + output + Style.RESET)
    else:
        print(start + Style.RESET, end='')
        print(output)

def error(output):
    start = Style.BOLD + Style.BG_RED + "ERROR:" + Style.RESET + " "
    if isinstance(output, str):
        print(start + output + Style.RESET)
    else:
        print(start + Style.RESET)
        print(output, end='')

class LineColor:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    PURPLE = (255, 0, 255)

lines = []
lineColor = LineColor.RED
window = {}

class Line:
    def __init__(self, start: tuple, end: tuple):
        self.start = start
        self.end = end
        self.color = lineColor

def set_line_color(color: LineColor):
    global lineColor
    lineColor = color

def set_window(surface):
    global window
    window = surface

def add_line(start: tuple, end: tuple):
    lines.append(Line(start, end))

def add_lines(points: list[tuple], loop: bool):
    i = 1
    length = len(points)
    for point in points:
        if i < length:
            add_line((point[0], point[1]), (points[i][0], points[i][1]))
        i += 1
    if loop:
        add_line((points[0][0], points[0][1]), (points[length - 1][0], points[length - 1][1]))

def add_wire_square(x, y, width, height):
    add_lines([(x, y), (x, y + height), (x + width, y + height), (x + width, y)], True)

def draw_lines():
    global lines
    for line in lines:
        pygame.draw.line(window, line.color, line.start, line.end, 2)
    lines = []