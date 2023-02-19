from src_poc.Input import Input
from src_poc.Renderer import Renderer
from src_poc.Text import Text
import src_poc.Logger as Logger
from src_poc.GameManager import GameManager

class LoggerPoC(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        Text('Proof of Concept: Logging', rend, 20, (0, 0, 225), (0, 255, 255), 0, 0)

        # Demonstration logs
        Logger.info(Logger.Style.BOLD + Logger.Style.BG_RED + 'Hello ' + Logger.Style.RESET + Logger.Style.BLUE + 'World!')
        Logger.error('Hello ' + Logger.Style.BG_VIOLET + 'World!' + Logger.Style.RESET)

    def on_update(self):
        # Examples of drawing lines with the logger
        # Draws a blue triangle
        Logger.set_line_color(Logger.LineColor.BLUE)
        Logger.add_lines([(75, 75), (25, 125), (125, 125)], True)

        # Draws a red line
        Logger.set_line_color(Logger.LineColor.RED)
        Logger.add_lines([(700, 50), (600, 75), (650, 250), (500, 400)], False)

        # Draws a green square
        Logger.set_line_color(Logger.LineColor.GREEN)
        Logger.add_wire_square(200, 200, 100, 100)

        # Draws a purple point
        Logger.set_line_color(Logger.LineColor.PURPLE)
        Logger.add_wire_square(400, 400, 3, 3)