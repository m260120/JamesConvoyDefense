
import pygame
from gameparameters import *


class Strip(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/rd.png").convert()
        self.image_original_size = self.image.get_size()
        self.image_new_size = (self.image_original_size[0] * 3.33333334,   # Resizing strip
                               self.image_original_size[1]*1)
        self.image = pygame.transform.scale(self.image, self.image_new_size)
        self.image = pygame.transform.rotate(self.image, 90)
        self.image.set_colorkey((0, 0, 0))

        # Setting default starting position
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2,
                                                int(0 - self.image.get_height()/2) + 65))  # Default position for strip

    def update(self):  # Move the strip down the road
        self.rect.y += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)


strips = pygame.sprite.Group()  # Create a group to add multiple strips and cycle through them
