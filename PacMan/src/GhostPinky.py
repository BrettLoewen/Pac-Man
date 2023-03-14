import src.Logger as Logger
from src.Sprite import Sprite
from src.GameManager import GameManager
from src.Grid import GridCell, Grid, CELLS_IN_COLUMN, CELLS_IN_ROW
from src.Collider import Collider
import math
from src.GhostController import GhostController
from src.PacManController import PacManController
# from src.PacMan import PacMan

class GhostPinky(GhostController):
    def __init__(self, game_manager):
        GhostController.__init__(self, game_manager,"PacMan/res/textures/Pinky_Left_0.png")
    
    def calculate_target_cell(self):
        pacman: PacManController = self.game_manager.pacman
        direction = pacman.direction

        target_cell: GridCell = pacman.target_cell

        grid: Grid = self.game_manager.grid

        x = target_cell.grid_x
        y = target_cell.grid_y

        if direction == 0:
            y = max(0, min(CELLS_IN_ROW - 1, y - 2))
        elif direction == 1:
            x = max(0, min(CELLS_IN_COLUMN - 1, x + 2))
        elif direction == 2:
            y = max(0, min(CELLS_IN_ROW - 1, y + 2))
        elif direction == 3:
            x = max(0, min(CELLS_IN_COLUMN - 1, x - 2))

        target = max(0, min((CELLS_IN_COLUMN * CELLS_IN_ROW) - 1, (x * CELLS_IN_COLUMN) + y))

        target_cell = grid.cells[target]

        if target_cell == None or (target_cell.up == False and target_cell.right == False and target_cell.down == False and target_cell.left == False):
            target_cell = pacman.target_cell
        
        return target_cell