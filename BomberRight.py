import pygame
from gameparameters import *
import math


class BomberRight(pygame.sprite.Sprite):
    def __init__(self, x, y, ally_x, ally_y):
        super().__init__()
        self.image = pygame.image.load('./assets/bomber.png').convert()
        self.image_og_size = self.image.get_size()  # Resizing base, returns a tuple
        self.image_new_size = (self.image_og_size[0] * .5, self.image_og_size[1] * .5)
        self.image = pygame.transform.scale(self.image, self.image_new_size)

        self.health = 3  # Bombers take three hits to kill

        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x  # Variables for position of the center of rect
        self.y = y
        self.rect.center = (x, y)

        #  Given ally coordinates
        self.direction = (self.rect.center[0] - ally_x, self.rect.center[1] - ally_y)  # Find the direction
        length = math.hypot(self.direction[0], self.direction[1])  # Get unit vector and make it constant.
        # If you don't, jet will fly in variable directions
        self.direction = (self.direction[0] / length, - self.direction[1] / length)
        angle = math.degrees(math.atan2(-self.direction[1], self.direction[0]))
        # Get angle via angle made with unit vector

    def update(self, speed_x, speed_y, screen):
        self.y -= speed_y * self.direction[1]
        self.x += speed_x * self.direction[0]
        self.rect.x = self.x
        self.rect.y = self.y

        screen.blit(self.image, self.rect)


bomber_right_group = pygame.sprite.Group()
