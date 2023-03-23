import src.Logger as Logger
from src.Sprite import Sprite
from src.Collider import Collider

class Pellet():
    def __init__(self, x, y, rend, pellet_size, manager):
        self.x = x
        self.y = y

        self.sprite = Sprite('PacMan/res/textures/Pellet.png', x, y, rend, pellet_size)

        self.collider = Collider(x, y, pellet_size, pellet_size, "Pellet")
        self.manager = manager

    def disable(self):
        self.sprite.disable()
        self.collider.disable()

    def on_update(self):
        if self.collider.overlaps_collider_with_tag("PacMan"):
            self.manager.on_eat_pellet(self)
