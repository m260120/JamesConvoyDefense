
import pygame
from gameparameters import *


def draw_tank_base(screen):
    tank_base = pygame.image.load("./assets/tankbase.jpg").convert()
    tank_base_og_size = tank_base.get_size()  # Resizing base, returns a tuple
    tank_base_new_size = (tank_base_og_size[0] * .15, tank_base_og_size[1] * .15)
    tank_base = pygame.transform.scale(tank_base, tank_base_new_size)

    tank_base.set_colorkey((255, 255, 255))

    screen.blit(tank_base, (
    int(SCREEN_WIDTH / 2 - tank_base.get_width() / 2), int(SCREEN_HEIGHT / 2 - tank_base.get_height() / 2 + 30)))
