from src.Sprite import Sprite
from src.Input import Input
from src.Renderer import Renderer
from src.GameManager import GameManager
from src.Grid import Grid

SIZE_MULTIPLIER = 3
ENTITY_SIZE = 13 * SIZE_MULTIPLIER
GRID_CELL_SIZE = 23 * SIZE_MULTIPLIER

class PacMan(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        self.grid = Grid(rend, GRID_CELL_SIZE)

        self.x = 50
        self.y = 50
        self.width = ENTITY_SIZE
        self.height = ENTITY_SIZE
        self.speed = 2

        # Create an animated sprite
        self.sprite = Sprite(['PacMan/res/textures/PacMan_0.png', 'PacMan/res/textures/PacMan_1.png', 'PacMan/res/textures/PacMan_2.png', 'PacMan/res/textures/PacMan_1.png'], self.x, self.y, rend, ENTITY_SIZE)


    def on_update(self):
        # If the user has pressed movement keys, move the sprite
        if self.input.pressed_left():
            self.sprite.x -= self.speed
            self.sprite.set_rotation(180)
        if self.input.pressed_right():
            self.sprite.x += self.speed
            self.sprite.set_rotation(0)
        if self.input.pressed_up():
            self.sprite.y -= self.speed
            self.sprite.set_rotation(90)
        if self.input.pressed_down():
            self.sprite.y += self.speed
            self.sprite.set_rotation(-90)