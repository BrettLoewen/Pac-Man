from src_poc.Input import Input
from src_poc.Renderer import Renderer

class GameManager:
    # This constructor sets up the necessary variables for child classes
    # Subclasses are meant to add functionality to it and call super().__init__(rend, input)
    def __init__(self, rend: Renderer, input: Input):
        self.rend = rend
        self.input = input

    # This method is meant to be overriden by subclasses
    def on_update(self):
        pass