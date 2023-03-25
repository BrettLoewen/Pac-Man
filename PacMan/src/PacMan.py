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
from src.Pellet import Pellet
from src.Text import Text

POWER_MODE_TIME = 10

class PacMan(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        self.SIZE_MULTIPLIER = 3
        self.ENTITY_SIZE = 13 * self.SIZE_MULTIPLIER
        self.GRID_CELL_SIZE = 23 * self.SIZE_MULTIPLIER
        self.PELLET_SIZE = 8 * 2

        self.grid = Grid(rend, self.GRID_CELL_SIZE)

        self.pellets = []
        for cell in self.grid.cells:
            if cell.pellet > 0:
                x = (cell.grid_x * self.GRID_CELL_SIZE) + (self.GRID_CELL_SIZE // 2) - (self.PELLET_SIZE // 2)
                y = (cell.grid_y * self.GRID_CELL_SIZE) + (self.GRID_CELL_SIZE // 2) - (self.PELLET_SIZE // 2)
                self.pellets.append(Pellet(x, y, rend, self.PELLET_SIZE, cell.pellet, self))

        self.pacman = PacManController(self)

        self.ghost_red = GhostBlinky(self)
        self.ghost_pink = GhostPinky(self)
        self.ghost_blue = GhostInky(self)
        self.ghost_orange = GhostClyde(self)

        self.score = 0
        self.score_text = Text('Score: ' + str(self.score), self.rend, 20, (0, 0, 0), (9, 6, 245), 0, 375)

        self.power_mode = 0
        self.power_text = Text('Power: ' + str(self.power_mode), self.rend, 20, (0, 0, 0), (9, 6, 245), 0, 400)

        # Collision.set_draw_colliders(True)

    def set_frame_info(self, frame, frame_rate):
        self.frame = frame
        self.frame_rate = frame_rate

    def on_update(self):
        self.pacman.on_update()

        self.ghost_red.on_update()
        self.ghost_pink.on_update()
        self.ghost_blue.on_update()
        self.ghost_orange.on_update()

        if self.frame == 0 and self.power_mode > 0:
            self.power_mode -= 1

        for pellet in self.pellets:
            pellet.on_update()

        if self.frame % 10 == 0:
            Collision.check_collisions()
        
        self.score_text.string = 'Score: ' + str(self.score)
        self.power_text.string = 'Score: ' + str(self.power_mode)

    def on_eat_pellet(self, pellet):
        self.pellets.remove(pellet)
        pellet.disable()
        self.score += 10

        # If the pellet is a power pellet, enter power mode
        if pellet.type == 2:
            self.power_mode = POWER_MODE_TIME
