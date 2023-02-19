import pygame
from src_poc.Renderer import Renderer
from src_poc.Input import Input
import src_poc.Logger as Logger

from src_poc.InputPoC import InputPoC
from src_poc.LoggerPoC import LoggerPoC
from src_poc.CollisionPoC import CollisionPoC
from src_poc.FilePoC import FilePoC

# Start pygame
pygame.init()

# Create the game window and set its size and name
window = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Proof of Concept")

# Create the clock to manage time and set the frame rate
clock = pygame.time.Clock()
frame_rate = 60
frame = 10

# Create the object which will handle rendering
rend = Renderer(window)

# Create the object which will handle user input
input = Input()

# Tell the logger which window to draw on
Logger.set_window(window)

# --- Select Proof of Concept here ---
# Create the object which will run the game
game = InputPoC(rend, input)
# game = LoggerPoC(rend, input)
# game = CollisionPoC(rend, input)
# game = FilePoC(rend, input)

# Main loop
run = True
while run:
    # Set the frame rate
    clock.tick(frame_rate)

    # Increment the frame counter
    frame = (frame + 1) % frame_rate

    # Stops the game loop if the user pressed the window's quit button
    run = input.still_running()
    
    # Get the keys the user has pressed
    input.process_input()

    # Run the game logic
    game.on_update()

    # Draw the game
    rend.draw_game_window(frame, frame_rate)

# If this point is reached, close the window
pygame.quit()