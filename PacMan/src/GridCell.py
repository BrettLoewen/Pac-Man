import src.Logger as Logger
from src.Sprite import Sprite

WHITE = (255, 255, 255)

class GridCell:
    def __init__(self, up, right, down, left, x, y, cell_size, rend):
        self.up = up == WHITE
        self.right = right == WHITE
        self.down = down == WHITE
        self.left = left == WHITE

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