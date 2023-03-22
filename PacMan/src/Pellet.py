import src.Logger as Logger
from src.Sprite import Sprite

class Pellet():
    def __init__(self, x, y, rend, pellet_size):
        self.x = x
        self.y = y

        self.sprite = Sprite('PacMan/res/textures/Pellet.png', x, y, rend, pellet_size)