
import pygame
from gameparameters import *


class Ally(pygame.sprite.Sprite):
    def __init__(self, x, y, file_path, scale):
        super().__init__()
        self.image = pygame.image.load(str(file_path))
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.rotate(self.image, -90)
        self.image_og_size = self.image.get_size()
        self.image_new_size = (self.image_og_size[0] * float(scale), self.image_og_size[1] * float(scale))
        self.image = pygame.transform.scale(self.image, self.image_new_size)

        self.rect = self.image.get_rect(center=(x, y))
        self.rect.center = (x, y)

    def draw_ally(self, screen):
        screen.blit(self.image, self.rect)


allies = pygame.sprite.Group()
