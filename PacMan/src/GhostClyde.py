import src.Logger as Logger
from src.Grid import GridCell, Grid, CELLS_IN_COLUMN, CELLS_IN_ROW
from src.GhostController import GhostController
from src.PacManController import PacManController

class GhostClyde(GhostController):
    def __init__(self, game_manager):
        GhostController.__init__(self, game_manager,"PacMan/res/textures/Clyde_Left_0.png")
    
    def calculate_target_cell(self):
        return self.current_cell