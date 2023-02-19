import pygame

class Sprite:
    def __init__(self, image_path, x, y, renderer):
        self.generate_images(image_path)
        self.x = x
        self.y = y
        self.angle = 0
        self.rend = renderer
        renderer.add_sprite(self) # This allows the sprite to be drawn

    # Sets the image's size
    def set_scale(self, x_scale, y_scale):
        i = 0
        for image in self.images:
            self.images[i] = pygame.transform.scale(image, (x_scale, y_scale))
            i += 1

    # Sets the sprite's angle variable which is used below to rotate the image before drawing
    def set_rotation(self, angle):
        self.angle = angle
    
    def get_center(self):
        return (self.x +  self.images[0].get_width() / 2, self.y + self.images[0].get_height() / 2)

    def get_image(self, frame, frame_rate):
        return pygame.transform.rotate(self.images[frame // (frame_rate // len(self.images))], self.angle)

    def get_rect(self, frame, frame_rate):
        return self.get_image(frame, frame_rate).get_rect(center=self.get_center())

    def generate_images(self, image_path):
        self.images = []
        if(isinstance(image_path, list)):
            for path in image_path:
                self.images.append(pygame.image.load(path))
        elif(isinstance(image_path, str)):
            self.images.append(pygame.image.load(image_path))