import math

import pygame
from gameparameters import *
from math import cos, sin, atan2, hypot, degrees


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Every time a bullet is created, these are re-defined for the specific bullet
        self.image = pygame.image.load('./assets/tankshell.png')
        self.image.set_colorkey((255, 255, 255))
        self.image_og_size = self.image.get_size()  # Resizing, returns a tuple
        self.image_new_size = (self.image_og_size[0] * .02, self.image_og_size[1] * .02)
        self.image = pygame.transform.scale(self.image, self.image_new_size)

        #  Rotating towards mouse and staying at that angle
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        mouse_x, mouse_y = pygame.mouse.get_pos()  # When a bullet is generated, get mouse position
        self.direction = (mouse_x - x, mouse_y - y)  # Find the direction via distance formula
        length = hypot(self.direction[0], self.direction[1])  # Get unit vector and make it constant.
        # If you don't, bullet will fly in variable directions
        self.direction = (self.direction[0]/length, self.direction[1]/length)
        angle = degrees(atan2(-self.direction[1], self.direction[0]))
        # Get angle via angle made with unit vector

        if 0 < angle < 90:  # Offset rotations based on different quadrants, trial and error
            self.image = pygame.transform.rotate(self.image, angle - 90)
        elif -90 < angle < 0:
            self.image = pygame.transform.rotate(self.image, angle - 90)
        elif 90 < angle < 180:
            self.image = pygame.transform.rotate(self.image, angle - 90)
        elif -180 < angle < -90:
            self.image = pygame.transform.rotate(self.image, angle - 90)

        self.image.set_colorkey((255, 255, 255))

    def update(self):
        self.x += BULLET_SPEED * self.direction[0]  # Update position based on lengths of unit vector
        self.y += BULLET_SPEED * self.direction[1]

        self.rect.x, self.rect.y = self.x, self.y  # Update rectangle

    def draw_bullet(self, screen):
        screen.blit(self.image, self.rect)

    def get_bullet_rect(self):
        return self.image


bullets = pygame.sprite.Group()

