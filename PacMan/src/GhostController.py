import src.Logger as Logger
from src.Sprite import Sprite
from src.GameManager import GameManager
from src.Grid import GridCell
from src.Collider import Collider
import math

SPEED = 1.2

class GhostController:
    def __init__(self, game_manager, texture, color_name):
        self.game_manager = game_manager

        self.color_name = color_name

        self.starting_cell = self.game_manager.grid.cells[48]
        x = self.starting_cell.x + (self.game_manager.GRID_CELL_SIZE // 2) + (self.game_manager.ENTITY_SIZE // 2)
        y = self.starting_cell.y + (self.game_manager.GRID_CELL_SIZE // 2) - (self.game_manager.ENTITY_SIZE // 2)
        self.width = self.game_manager.ENTITY_SIZE
        self.height = self.game_manager.ENTITY_SIZE
        self.speed = SPEED

        self.collider = Collider(x, y, game_manager.ENTITY_SIZE, game_manager.ENTITY_SIZE, "Ghost")

        self.sprite = Sprite(texture, x, y, game_manager.rend, self.game_manager.ENTITY_SIZE)

        self.prev_target = self.game_manager.pacman.target_cell
        self.path = []
        self.current_cell = self.starting_cell
        self.next_cell = self.current_cell

        self.direction = -1

    def on_update(self):
        if self.prev_target != self.calculate_target_cell():
            self.prev_target = self.calculate_target_cell()
            current_cell = self.current_cell if self.next_cell == None else self.next_cell
            self.path = self.find_path(self.prev_target, current_cell)

        # Logger.set_line_color(Logger.LineColor.PURPLE)
        # points = []
        # for cell in self.path:
        #     points.append((cell.x + (self.game_manager.GRID_CELL_SIZE // 2), cell.y + (self.game_manager.GRID_CELL_SIZE // 2)))
        # Logger.add_lines(points, False)

        self.move()

        self.collider.x = self.sprite.x
        self.collider.y = self.sprite.y

        if self.collider.overlaps_collider_with_tag("PacMan"):
            self.game_manager.on_ghost_hit_pacman(self)

    def calculate_target_cell(self):
        return self.game_manager.pacman.target_cell

    def move(self):
        if self.next_cell == None:
            if len(self.path) > 0:
                self.next_cell = self.path.pop()
            else:
                # Do nothing
                pass
        else:
            sprite_center_x = self.sprite.get_center()[0]
            sprite_center_y = self.sprite.get_center()[1]
            cell_center_x = self.next_cell.x + (self.game_manager.GRID_CELL_SIZE // 2)
            cell_center_y = self.next_cell.y + (self.game_manager.GRID_CELL_SIZE // 2)
            diff_x = sprite_center_x - cell_center_x
            diff_y = sprite_center_y - cell_center_y

            # If the ghost has reached the center of their next cell
            if math.dist((cell_center_x, cell_center_y), (sprite_center_x, sprite_center_y)) < 2:
                self.current_cell = self.next_cell
                self.next_cell = self.path.pop() if len(self.path) > 0 else None
                self.direction = -1
                self.sprite.x = cell_center_x - (self.game_manager.ENTITY_SIZE // 2)
                self.sprite.y = cell_center_y - (self.game_manager.ENTITY_SIZE // 2)
            # If the ghost has not reached the center of their next cell, set the movement direction
            else:
                self.calculate_direction(diff_x, diff_y)
        
        if self.direction == 0:
            self.sprite.y -= self.speed
        elif self.direction == 1:
            self.sprite.x += self.speed
        elif self.direction == 2:
            self.sprite.y += self.speed
        elif self.direction == 3:
            self.sprite.x -= self.speed

    def calculate_direction(self, diff_x, diff_y):
        if abs(diff_x) > abs(diff_y):
            if diff_x < 1:
                self.direction = 1
            elif diff_x > 0:
                self.direction = 3
        else:
            if diff_y < 0:
                self.direction = 2
            elif diff_y > 0:
                self.direction = 0

    def find_path(self, target_cell, start_cell):
        # Reset every cell's pathfinding variables
        for cell in self.game_manager.grid.cells:
            cell.reset_costs()
        
        # Create empty lists for storing pathfinding info
        path = []
        open_cells = []
        closed_cells = []

        # Start at the passed start point
        open_cells.append(start_cell)

        diff_x = target_cell.x - start_cell.x
        diff_y = target_cell.y - start_cell.y
        start_cell.h_cost = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
        start_cell.g_cost = 0
        start_cell.f_cost = start_cell.h_cost

        found_path = self.calculate_path(open_cells, closed_cells, target_cell)

        if found_path == False:
            for cell in self.game_manager.grid.cells:
                cell.reset_costs()
            open_cells = []
            closed_cells = []
            open_cells.append(start_cell)
            self.calculate_path(open_cells, closed_cells, self.game_manager.pacman.target_cell)
        
        # Loop backwards through the found path and store it in a list so it can be returned
        prev = target_cell
        while prev != None:
            path.append(prev)
            prev = prev.parent

        # Return the found path to the destination
        return path

    def calculate_path(self, open_cells, closed_cells, target_cell):
        # Loop through cells (using A*) until we find a path to the target cell
        found_path = False
        while(len(open_cells) > 0):
            # Get the next cell to check
            current: GridCell = self.get_lowest_f_cost_cell(open_cells)
            open_cells.remove(current)
            closed_cells.append(current)

            # If we found the destination, stop, our job is done
            if current == target_cell:
                found_path = True
                break

            # Loop through the current cell's neighbours
            for cell in current.connections:
                # If the neighbour has already been visited, ignore it
                if closed_cells.__contains__(cell):
                    # Do nothing
                    pass
                # If a shorter path has been found, check it
                elif open_cells.__contains__(cell):
                    diff_x = current.x - self.sprite.x
                    diff_y = current.y - self.sprite.y
                    temp_g_cost = current.g_cost + math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))

                    if temp_g_cost < cell.g_cost:
                        cell.parent = current
                        cell.g_cost = temp_g_cost
                        cell.f_cost = cell.g_cost + cell.h_cost
                # If the neighbour has not been checked yet, check it
                else:
                    # Set the neighbour's cost and path
                    cell.set_costs(target_cell, current)
                    cell.parent = current

                    # Add the neighbour to the open list so it can be visited later
                    open_cells.append(cell)

        if found_path == False:
            Logger.error("No path was found")
            return False
        return True

    # Determine which cell to check next
    def get_lowest_f_cost_cell(self, openCells):
        # Setup
        lowest_cost = 1000000
        lowest_cost_cell = openCells[0]

        # Loop through every open cell
        for cell in openCells:
            # If the cell has a lower f cost
            if cell.f_cost < lowest_cost:
                lowest_cost_cell = cell # Set its f cost as the standard
                lowest_cost = cell.f_cost # Store it so it can be returned if nothing closer is found

        # Return the cell with the lowest f cost
        return lowest_cost_cell
    
    def die(self):
        self.sprite.disable()
        self.collider.disable()