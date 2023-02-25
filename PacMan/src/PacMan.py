import src.Logger as Logger
from src.Sprite import Sprite
from src.Input import Input
from src.Renderer import Renderer
from src.GameManager import GameManager
from src.Grid import Grid
from src.Grid import GridCell
import math
from src.PacManController import PacManController

class PacMan(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        self.SIZE_MULTIPLIER = 3
        self.ENTITY_SIZE = 13 * self.SIZE_MULTIPLIER
        self.GRID_CELL_SIZE = 23 * self.SIZE_MULTIPLIER

        self.grid = Grid(rend, self.GRID_CELL_SIZE)

        self.pacman = PacManController(self)

        starting_cell = self.grid.cells[48]
        self.x = starting_cell.x + (self.GRID_CELL_SIZE // 2) + (self.ENTITY_SIZE // 2)
        self.y = starting_cell.y + (self.GRID_CELL_SIZE // 2) - (self.ENTITY_SIZE // 2)
        self.width = self.ENTITY_SIZE
        self.height = self.ENTITY_SIZE
        self.speed = 2
        self.sprite = Sprite("PacMan/res/textures/Inky_Left_0.png", self.x, self.y, rend, self.ENTITY_SIZE)

    def on_update(self):
        self.pacman.on_update()

    def find_path(self):
        path = []

        