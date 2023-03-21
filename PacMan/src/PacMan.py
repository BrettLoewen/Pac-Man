import src.Logger as Logger
from src.Sprite import Sprite
from src.Input import Input
from src.Renderer import Renderer
from src.GameManager import GameManager
from src.Grid import Grid
from src.Grid import GridCell
import math
from src.PacManController import PacManController
from src.GhostController import GhostController
import src.CollisionManager as Collision
from src.GhostBlinky import GhostBlinky
from src.GhostPinky import GhostPinky
from src.GhostInky import GhostInky
from src.GhostClyde import GhostClyde

class PacMan(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        self.SIZE_MULTIPLIER = 3
        self.ENTITY_SIZE = 13 * self.SIZE_MULTIPLIER
        self.GRID_CELL_SIZE = 23 * self.SIZE_MULTIPLIER

        self.grid = Grid(rend, self.GRID_CELL_SIZE)

        self.pacman = PacManController(self)

        # self.ghost = GhostBlinky(self)
        # self.ghost = GhostPinky(self)
        self.ghost = GhostInky(self)
        # self.ghost = GhostClyde(self)

        # Collision.set_draw_colliders(True)

    def on_update(self):
        self.pacman.on_update()

        self.ghost.on_update()

        Collision.check_collisions()