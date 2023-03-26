import src.Logger as Logger
from src.Grid import GridCell, Grid, CELLS_IN_COLUMN, CELLS_IN_ROW
from src.GhostController import GhostController
from src.PacManController import PacManController

class GhostInky(GhostController):
    def __init__(self, game_manager):
        GhostController.__init__(self, game_manager,"PacMan/res/textures/Inky_Left_0.png", "blue")
    
    def calculate_target_cell(self):
        # Get the necessary references for the AI
        pacman: PacManController = self.game_manager.pacman
        target_cell: GridCell = pacman.target_cell
        current_cell: GridCell = self.current_cell
        grid: Grid = self.game_manager.grid

        # Get the coordinates relevant to pathfinding
        target_x = target_cell.grid_x
        target_y = target_cell.grid_y
        my_x = current_cell.grid_x
        my_y = current_cell.grid_y

        # Get the ideal target cell
        diff_x = target_x + (target_x - my_x)
        diff_y = target_y + (target_y - my_y)
        
        # Bind the target cell within the grid
        diff_x = max(0, min(CELLS_IN_COLUMN - 1, diff_x))
        diff_y = max(0, min(CELLS_IN_ROW - 1, diff_y))

        # Get the target cell's index in the grid
        target = max(0, min((CELLS_IN_COLUMN * CELLS_IN_ROW) - 1, (diff_x * CELLS_IN_COLUMN) + diff_y))

        # Get the target cell
        target_cell = grid.cells[target]

        # If the target cell can not be moved to, target Pacman directly
        if target_cell == None or (target_cell.up == False and target_cell.right == False and target_cell.down == False and target_cell.left == False):
            target_cell = pacman.target_cell
        
        # Return the calculated target cell
        return target_cell