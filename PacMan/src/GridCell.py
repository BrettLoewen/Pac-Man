import src.Logger as Logger
from src.Sprite import Sprite

WHITE = (255, 255, 255)

class GridCell:
    def __init__(self, up, right, down, left, x, y, cell_size, rend):
        self.up = up == WHITE
        self.right = right == WHITE
        self.down = down == WHITE
        self.left = left == WHITE

        self.up_cell = None
        self.right_cell = None
        self.down_cell = None
        self.left_cell = None

        self.x = x
        self.y = y

        direction = 0
        if self.up:
            direction += 1
        if self.right:
            direction += 2
        if self.down:
            direction += 4
        if self.left:
            direction += 8
        self.direction = direction

        sprite_name = "PacMan/res/textures/Map_" + str(direction) + ".png"
        self.sprite = Sprite(sprite_name, x, y, rend, cell_size)

        self.connections = []

    def add_connection(self, connected_cell, direction):
        self.connections.append(connected_cell)

        if direction == 0:
            self.up_cell = connected_cell
        if direction == 1:
            self.right_cell = connected_cell
        if direction == 2:
            self.down_cell = connected_cell
        if direction == 3:
            self.left_cell = connected_cell

    def check_direction(self, direction):
        return self.get_connected_cell(direction) != None

    def get_connected_cell(self, direction):
        if direction == 0:
            return self.up_cell
        if direction == 1:
            return self.right_cell
        if direction == 2:
            return self.down_cell
        if direction == 3:
            return self.left_cell
        return None
