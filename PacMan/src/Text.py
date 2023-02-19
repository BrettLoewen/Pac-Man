import pygame

class Text:
    def __init__(self, string, renderer, fontSize = 32, bgColor = (0, 0, 0), textColor = (255, 255, 255), x = 0, y = 0):
        self.string = string
        self.bgColor = bgColor
        self.textColor = textColor
        self.fontSize = fontSize
        self.font = 'freesansbold.ttf'
        self.x = x
        self.y = y
        renderer.add_text(self)