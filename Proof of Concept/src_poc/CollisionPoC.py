from src_poc.Input import Input
from src_poc.Renderer import Renderer
from src_poc.Text import Text
import src_poc.Logger as Logger
from src_poc.GameManager import GameManager
from src_poc.Collider import Collider
import src_poc.CollisionManager as CollisionManager

class CollisionPoC(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        Text('Proof of Concept: Collision', rend, 20, (0, 0, 225), (0, 255, 255), 0, 0)

        # Create the colliders
        self.collider1 = Collider(203, 212, 100, 100, "PacMan")
        self.collider2 = Collider(350, 350, 100, 100, "Ghost")
        self.collider3 = Collider(450, 450, 100, 100, "Ghost")
        self.collider4 = Collider(150, 150, 100, 100, "Pellet")
        self.collider5 = Collider(50, 50, 100, 100, "Pellet")
        self.speed = 3

        # CollisionManager.set_draw_colliders(False)
        CollisionManager.set_draw_colliders(True)

    def on_update(self):
        # If the user has pressed movement keys, move the collider
        if self.input.pressed_left():
            self.collider1.x -= self.speed
        if self.input.pressed_right():
            self.collider1.x += self.speed
        if self.input.pressed_up():
            self.collider1.y -= self.speed
        if self.input.pressed_down():
            self.collider1.y += self.speed

        # Check for collisions
        CollisionManager.check_collisions()

        Logger.info("Overlaps with a pellet: " + str(self.collider1.overlaps_collider_with_tag("Pellet")))