import pygame

class Input:
    def __init__(self):
        self.keys = []
    
    # Get the keys the user has pressed
    def process_input(self):
        self.keys = pygame.key.get_pressed()

    # Check if the user pressed the quit button. 
    # Returns False if they did, and True if they didn't
    def still_running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    # Checks and returns whether or not the user pressed the left key
    def pressed_left(self):
        return self.keys[pygame.K_LEFT]

    # Checks and returns whether or not the user pressed the right key
    def pressed_right(self):
        return self.keys[pygame.K_RIGHT]

    # Checks and returns whether or not the user pressed the up key
    def pressed_up(self):
        return self.keys[pygame.K_UP]

    # Checks and returns whether or not the user pressed the down key
    def pressed_down(self):
        return self.keys[pygame.K_DOWN]

    # Checks and returns whether or not the user pressed the 'a' key
    def pressed_a(self):
        return self.keys[pygame.K_a]

    # Checks and returns whether or not the user pressed the 'd' key
    def pressed_d(self):
        return self.keys[pygame.K_d]

    # Checks and returns whether or not the user pressed the 'w' key
    def pressed_w(self):
        return self.keys[pygame.K_w]

    # Checks and returns whether or not the user pressed the 's' key
    def pressed_s(self):
        return self.keys[pygame.K_s]
