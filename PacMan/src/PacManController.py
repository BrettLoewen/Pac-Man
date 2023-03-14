import src.Logger as Logger
from src.Sprite import Sprite
from src.GameManager import GameManager
from src.Collider import Collider
import math

SPEED = 2

class PacManController():
    def __init__(self, game_manager: GameManager):
        self.game_manager = game_manager
        self.input = self.game_manager.input

        starting_cell = self.game_manager.grid.cells[52]
        x = starting_cell.x + (game_manager.GRID_CELL_SIZE // 2) + (game_manager.ENTITY_SIZE // 2)
        y = starting_cell.y + (game_manager.GRID_CELL_SIZE // 2) - (game_manager.ENTITY_SIZE // 2)
        self.width = game_manager.ENTITY_SIZE
        self.height = game_manager.ENTITY_SIZE
        self.speed = SPEED

        self.collider = Collider(x, y, game_manager.ENTITY_SIZE, game_manager.ENTITY_SIZE, "PacMan")

        # Create an animated sprite
        image_paths = ['PacMan/res/textures/PacMan_0.png', 'PacMan/res/textures/PacMan_1.png', 'PacMan/res/textures/PacMan_2.png', 'PacMan/res/textures/PacMan_1.png']
        self.sprite = Sprite(image_paths, x, y, game_manager.rend, game_manager.ENTITY_SIZE)
        self.sprite.set_rotation(180)
        self.direction = 3
        self.input_direction = 3
        self.target_cell = starting_cell

    def on_update(self):
        # If the user has pressed movement keys, move the sprite
        if self.input.pressed_left():
            self.input_direction = 3
        if self.input.pressed_right():
            self.input_direction = 1
        if self.input.pressed_up():
            self.input_direction = 0
        if self.input.pressed_down():
            self.input_direction = 2

        sprite_center_x = self.sprite.get_center()[0]
        sprite_center_y = self.sprite.get_center()[1]
        cell_center_x = self.target_cell.x + (self.game_manager.GRID_CELL_SIZE // 2)
        cell_center_y = self.target_cell.y + (self.game_manager.GRID_CELL_SIZE // 2)
        diff_x = sprite_center_x - cell_center_x
        diff_y = sprite_center_y - cell_center_y
        distance = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
        if distance < 1:
            self.sprite.x = cell_center_x - (self.game_manager.ENTITY_SIZE // 2)
            self.sprite.y = cell_center_y - (self.game_manager.ENTITY_SIZE // 2)
            
            input_check = self.target_cell.check_direction(self.input_direction)
            
            if input_check:
                self.direction = self.input_direction
                self.target_cell = self.target_cell.get_connected_cell(self.direction)
            else:
                self.direction = -1

        if self.direction == 0:
            self.sprite.y -= self.speed
            self.sprite.set_rotation(90)
        elif self.direction == 1:
            self.sprite.x += self.speed
            self.sprite.set_rotation(0)
        elif self.direction == 2:
            self.sprite.y += self.speed
            self.sprite.set_rotation(-90)
        elif self.direction == 3:
            self.sprite.x -= self.speed
            self.sprite.set_rotation(180)

        self.collider.x = self.sprite.x
        self.collider.y = self.sprite.y

        # Logger.info(self.collider.overlaps_collider_with_tag("Ghost"))
        
        # Logger.set_line_color(Logger.LineColor.GREEN)
        for cell in self.game_manager.grid.cells:
            offset = self.game_manager.GRID_CELL_SIZE // 2
            start_pos: tuple = (cell.x + offset, cell.y + offset)
            for connection in cell.connections:
                end_pos: tuple = (connection.x + offset, connection.y + offset)
                # Logger.add_line(start_pos, end_pos)

        # Logger.set_line_color(Logger.LineColor.RED)
        # Logger.add_line((sprite_center_x, sprite_center_y), (cell_center_x, cell_center_y))