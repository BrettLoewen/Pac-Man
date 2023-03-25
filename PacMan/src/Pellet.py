import src.Logger as Logger
from src.Sprite import Sprite
from src.Collider import Collider

PELLET_TEXTURE = 'PacMan/res/textures/Pellet.png'
POWER_PELLET_TEXTURE = 'PacMan/res/textures/Power_Pellet.png'

class Pellet():
    def __init__(self, x, y, rend, pellet_size, pellet_type, manager):
        self.x = x
        self.y = y

        self.type = pellet_type

        texture = PELLET_TEXTURE
        if pellet_type == 2:
            texture = POWER_PELLET_TEXTURE
        self.sprite = Sprite(texture, x, y, rend, pellet_size)

        self.collider = Collider(x, y, pellet_size, pellet_size, "Pellet")
        self.manager = manager

    def disable(self):
        self.sprite.disable()
        self.collider.disable()

    def on_update(self):
        if self.collider.overlaps_collider_with_tag("PacMan"):
            self.manager.on_eat_pellet(self)
