import pygame
from src.Renderer import Renderer
from src.Input import Input
import src.Logger as Logger
from src.GameManager import GameManager

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

# Create the object which will run the game
game = GameManager(rend, input)

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