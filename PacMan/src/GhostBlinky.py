import src.Logger as Logger
from src.Sprite import Sprite
from src.GameManager import GameManager
from src.Grid import GridCell
from src.Collider import Collider
import math
from src.GhostController import GhostController

class GhostBlinky(GhostController):
    def __init__(self, game_manager: GameManager):
        GhostController.__init__(self, game_manager,"PacMan/res/textures/Blinky_Left_0.png")
    
    def calculate_target_cell(self):
        return super().calculate_target_cell()