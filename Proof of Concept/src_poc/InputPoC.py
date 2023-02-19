from src_poc.Sprite import Sprite
from src_poc.Input import Input
from src_poc.Renderer import Renderer
from src_poc.Text import Text
from src_poc.GameManager import GameManager

class InputPoC(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        Text('Proof of Concept: Input', rend, 20, (0, 0, 225), (0, 255, 255), 0, 0)

        self.x = 50
        self.y = 50
        self.width = 64
        self.height = 64
        self.speed = 5

        # Create an animated sprite
        self.sprite = Sprite(['Proof of Concept/res/textures/PacMan_0.png', 'Proof of Concept/res/textures/PacMan_1.png', 'Proof of Concept/res/textures/PacMan_2.png', 'Proof of Concept/res/textures/PacMan_1.png'], self.x, self.y, rend)
        self.sprite.set_scale(self.width, self.height)

        # Create an animated sprite
        self.sprite2 = Sprite(['Proof of Concept/res/textures/PacMan_1.png'], self.x, self.y, rend)
        self.sprite2.set_scale(self.width, self.height)

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

        if self.input.pressed_a():
            self.sprite2.x -= self.speed
            self.sprite2.set_rotation(180)
        if self.input.pressed_d():
            self.sprite2.x += self.speed
            self.sprite2.set_rotation(0)
        if self.input.pressed_w():
            self.sprite2.y -= self.speed
            self.sprite2.set_rotation(90)
        if self.input.pressed_s():
            self.sprite2.y += self.speed
            self.sprite2.set_rotation(-90)