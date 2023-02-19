import pygame
from src_poc.Text import Text
import src_poc.Logger as Logger
import src_poc.CollisionManager as CollisionManager

class Renderer:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.sprites = []
        self.texts = []

    # Allows sprites to add themselves to the renderer's list of known sprites
    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    def draw_sprite(self, sprite, coords: tuple):
        self.window.blit(sprite, coords)
    
    def draw_sprites(self, frame, frame_rate):
        # Loop through every sprite that the renderer knows about
        for sprite in self.sprites:
            # Draw every sprite
            self.draw_sprite(sprite.get_image(frame, frame_rate), sprite.get_rect(frame, frame_rate))

    def add_text(self, text):
        self.texts.append(text)

    def draw_text(self, text: Text):
        font = pygame.font.Font(text.font, text.fontSize)
        drawText = font.render(text.string, True, text.textColor, text.bgColor)
        textRect = drawText.get_rect()
        textRect.left = text.x
        textRect.top = text.y

        # Draw the text
        self.window.blit(drawText, textRect)

    def draw_texts(self):
        for text in self.texts:
            self.draw_text(text)

    def draw_game_window(self, frame, frame_rate):
        # Cover up the previous render
        self.window.fill((0, 0, 0))

        # Draw the sprites (if any have been added)
        self.draw_sprites(frame, frame_rate)

        # Draw the texts (if any have been added)
        self.draw_texts()

        # Draw the colliders (if there are any to draw)
        CollisionManager.draw_colliders()

        # Draw the log lines (if any have been added)
        Logger.draw_lines()

        # Push the new draws to the window
        pygame.display.update()