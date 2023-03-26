import src.Logger as Logger
from src.Grid import GridCell, Grid, CELLS_IN_COLUMN, CELLS_IN_ROW
from src.GhostController import GhostController
from src.PacManController import PacManController
import math

SCARE_DISTANCE = 2
UNSCARE_DISTANCE = 1
TOP_LEFT_CELL = 24
TOP_RIGHT_CELL = 79
BOTTOM_LEFT_CELL = 20
BOTTOM_RIGHT_CELL = 97

class GhostClyde(GhostController):
    def __init__(self, game_manager):
        GhostController.__init__(self, game_manager,"PacMan/res/textures/Clyde_Left_0.png", "orange")
        self.scared = False
        self.current_scare_cell = None
    
    def calculate_target_cell(self):
        # Get the necessary references for the AI
        pacman: PacManController = self.game_manager.pacman
        target_cell: GridCell = pacman.target_cell
        current_cell: GridCell = self.current_cell
        grid: Grid = self.game_manager.grid
        prev_target_cell: GridCell = self.prev_target

        # Get the coordinates relevant to pathfinding
        target_x = target_cell.grid_x
        target_y = target_cell.grid_y
        my_x = current_cell.grid_x
        my_y = current_cell.grid_y

        # Calculate the distance between Clyde and PacMan
        distanceToPacMan = math.sqrt(((target_x - my_x) ** 2)+ ((target_y - my_y) ** 2))

        # If Clyde is too close to PacMan, he should become scared
        if distanceToPacMan <= SCARE_DISTANCE:
            self.scared = True

        # If Clyde is scared, check if he should stop being scared
        if self.scared:
            prev_target_x = prev_target_cell.grid_x
            prev_target_y = prev_target_cell.grid_y

            # Calculate the distance between Clyde and the cell he is running to
            distanceToScareCell = math.sqrt(((prev_target_x - my_x) ** 2)+ ((prev_target_y - my_y) ** 2))

            # If Clyde has reached a corner, stop being scared
            if distanceToScareCell < UNSCARE_DISTANCE:
                self.scared = False
                self.current_scare_cell = None

        # If Clyde is still scared, flee to the furthest corner
        if self.scared:
            target_cell = self.calculate_scare_cell(grid, my_x, my_y)

        # If the target cell can not be moved to, target PacMan directly
        if target_cell == None or (target_cell.up == False and target_cell.right == False and target_cell.down == False and target_cell.left == False):
            target_cell = pacman.target_cell
        
        # Return the calculated target cell
        return target_cell
    
    def calculate_scare_cell(self, grid: Grid, my_x: int, my_y: int):
        # Only calculate the cell to flee to if it has not already been calculated
        if self.current_scare_cell != None:
            target_cell = self.current_scare_cell
        else:
            # Get the possible scare cells
            corner_cells: list[GridCell] = []
            corner_cells.append(grid.cells[TOP_LEFT_CELL])
            corner_cells.append(grid.cells[TOP_RIGHT_CELL])
            corner_cells.append(grid.cells[BOTTOM_LEFT_CELL])
            corner_cells.append(grid.cells[BOTTOM_RIGHT_CELL])
            
            # Loop through the possible scare cells
            prev_distance = -1
            furthest_corner_cell = 0
            index = 0
            while index < len(corner_cells):
                # Get the corner cell's coordinates
                corner_x = corner_cells[index].grid_x
                corner_y = corner_cells[index].grid_y

                # Calculate the distance to the corner cell
                distanceToCornerCell = math.sqrt(((corner_x - my_x) ** 2)+ ((corner_y - my_y) ** 2))

                # If this corner cell is the furthest, store it
                if distanceToCornerCell > prev_distance:
                    prev_distance = distanceToCornerCell
                    furthest_corner_cell = index

                index += 1

            # Set the furthest corner cell from Clyde as the one he will run to
            target_cell = corner_cells[furthest_corner_cell]
            self.current_scare_cell = target_cell
        
        return target_cell