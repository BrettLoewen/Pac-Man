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
MAX_LIVES = 3
GHOST_PINK_DELAY = 5
GHOST_BLUE_DELAY = 10
GHOST_ORANGE_DELAY = 15
GHOST_RESPAWN_TIME = 10

class PacMan(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        self.SIZE_MULTIPLIER = 3
        self.ENTITY_SIZE = 13 * self.SIZE_MULTIPLIER
        self.GRID_CELL_SIZE = 23 * self.SIZE_MULTIPLIER
        self.PELLET_SIZE = 8 * 2

        self.reset()

        self.score_text = Text('Score: ' + str(self.score), self.rend, 20, (0, 0, 0), (9, 6, 245), 0, 375)
        self.power_text = Text('Power: ' + str(self.power_mode), self.rend, 20, (0, 0, 0), (9, 6, 245), 0, 400)
        self.lives_text = Text('Power: ' + str(self.lives), self.rend, 20, (0, 0, 0), (9, 6, 245), 0, 425)

        # Collision.set_draw_colliders(True)

    def set_frame_info(self, frame, frame_rate):
        self.frame = frame
        self.frame_rate = frame_rate

    def on_update(self):
        self.pacman.on_update()

        self.update_ghosts()

        if self.frame == 0 and self.power_mode > 0:
            self.power_mode -= 1

        for pellet in self.pellets:
            pellet.on_update()

        if self.frame % 10 == 0:
            Collision.check_collisions()

        if len(self.pellets) == 0:
            self.grid = Grid(self.rend, self.GRID_CELL_SIZE)
            self.setup()
        
        self.score_text.string = 'Score: ' + str(self.score)
        self.power_text.string = 'Power: ' + str(self.power_mode)
        self.lives_text.string = 'Lives: ' + str(self.lives)
        # Logger.info(self.score)

    def update_ghosts(self):
        # If the red ghost needs to be spawned
        if self.ghost_red == None and self.ghost_red_countdown <= 0:
            self.ghost_red = GhostBlinky(self)
        # If the red ghost is waiting to be spawned
        elif self.ghost_red == None and self.ghost_red_countdown > 0:
            if self.frame == 0:
                self.ghost_red_countdown -= 1
        # If the red ghost needs to update
        elif self.ghost_red != None and self.ghost_red_countdown <= 0:
            self.ghost_red.on_update()

        # If the blue ghost needs to be spawned
        if self.ghost_blue == None and self.ghost_blue_countdown <= 0:
            self.ghost_blue = GhostInky(self)
        # If the blue ghost is waiting to be spawned
        elif self.ghost_blue == None and self.ghost_blue_countdown > 0:
            if self.frame == 0:
                self.ghost_blue_countdown -= 1
        # If the blue ghost needs to update
        elif self.ghost_blue != None and self.ghost_blue_countdown <= 0:
            self.ghost_blue.on_update()
        
        # If the pink ghost needs to be spawned
        if self.ghost_pink == None and self.ghost_pink_countdown <= 0:
            self.ghost_pink = GhostPinky(self)
        # If the pink ghost is waiting to be spawned
        elif self.ghost_pink == None and self.ghost_pink_countdown > 0:
            if self.frame == 0:
                self.ghost_pink_countdown -= 1
        # If the pink ghost needs to update
        elif self.ghost_pink != None and self.ghost_pink_countdown <= 0:
            self.ghost_pink.on_update()

        # If the orange ghost needs to be spawned
        if self.ghost_orange == None and self.ghost_orange_countdown <= 0:
            self.ghost_orange = GhostClyde(self)
        # If the orange ghost is waiting to be spawned
        elif self.ghost_orange == None and self.ghost_orange_countdown > 0:
            if self.frame == 0:
                self.ghost_orange_countdown -= 1
        # If the orange ghost needs to update
        elif self.ghost_orange != None and self.ghost_orange_countdown <= 0:
            self.ghost_orange.on_update()

    def reset(self):
        self.score = 0
        self.lives = MAX_LIVES
        self.grid = Grid(self.rend, self.GRID_CELL_SIZE)
        self.setup()

    def setup(self):
        self.rend.remove_all_sprites()
        Collision.remove_all_colliders()

        self.grid.add_grid_sprites()

        self.pellets = []
        for cell in self.grid.cells:
            if cell.pellet > 0:
                x = (cell.grid_x * self.GRID_CELL_SIZE) + (self.GRID_CELL_SIZE // 2) - (self.PELLET_SIZE // 2)
                y = (cell.grid_y * self.GRID_CELL_SIZE) + (self.GRID_CELL_SIZE // 2) - (self.PELLET_SIZE // 2)
                self.pellets.append(Pellet(x, y, self.rend, self.PELLET_SIZE, cell.pellet, self, cell))

        self.pacman = PacManController(self)

        self.ghost_red = None
        self.ghost_pink = None
        self.ghost_blue = None
        self.ghost_orange = None
        self.ghost_red_countdown = 0
        self.ghost_blue_countdown = GHOST_PINK_DELAY
        self.ghost_pink_countdown = GHOST_BLUE_DELAY
        self.ghost_orange_countdown = GHOST_ORANGE_DELAY

        self.power_mode = 0

    def on_eat_pellet(self, pellet):
        self.pellets.remove(pellet)
        pellet.disable()
        self.score += 10

        # If the pellet is a power pellet, enter power mode
        if pellet.type == 2:
            self.power_mode = POWER_MODE_TIME

        pellet.cell.pellet = 0

    def on_ghost_hit_pacman(self, ghost: GhostController):
        # If PacMan can eat the ghost
        if self.power_mode > 0:
            if ghost.color_name == "red":
                self.ghost_red.die()
                self.ghost_red = None
                self.ghost_red_countdown = GHOST_RESPAWN_TIME
            if ghost.color_name == "pink":
                self.ghost_pink.die()
                self.ghost_pink = None
                self.ghost_pink_countdown = GHOST_RESPAWN_TIME
            if ghost.color_name == "blue":
                self.ghost_blue.die()
                self.ghost_blue = None
                self.ghost_blue_countdown = GHOST_RESPAWN_TIME
            if ghost.color_name == "orange":
                self.ghost_orange.die()
                self.ghost_orange = None
                self.ghost_orange_countdown = GHOST_RESPAWN_TIME
        # If PacMan should be killed by the ghost
        else:
            self.lives -= 1
            if self.lives <= 0:
                self.reset()
            else:
                self.setup()
