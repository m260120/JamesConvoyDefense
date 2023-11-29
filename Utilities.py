
from gameparameters import *
import random
from road import strips, Strip
from Bullet import bullets, Bullet
from jet1 import jet1group, Jet1
from jet2 import jet2group, Jet2
from BomberRight import BomberRight, bomber_right_group
from BomberLeft import BomberLeft, bomber_left_group


def draw_background(screen):

    grass = pygame.image.load("./assets/grass.png").convert()
    road = pygame.image.load("./assets/road.png").convert()

    grass.set_colorkey((0, 0, 0))
    road.set_colorkey((0, 0, 0))

    # Fill the screen with the grass, road, and tank base background:
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(grass, (x, y))
    for x in range(int((SCREEN_WIDTH/2) - TILE_SIZE), int((SCREEN_WIDTH/2) + TILE_SIZE), TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(road, (x, y))


def add_strips(num_strips):
    for num in range(num_strips):
        strips.add(Strip())


def add_bullets(num_bullets, pos):
    for num in range(num_bullets):
        bullets.add(Bullet(pos[0], pos[1]))


def add_jet2s_left(num_jets, ally_x, ally_y):
    for _ in range(num_jets):
        jet2group.add(Jet2(random.randint(-SCREEN_WIDTH * 5, -70),
                           random.randint(50, 550), ally_x, ally_y))


def add_jet1s_right(num_jets, ally_x, ally_y):
    for _ in range(num_jets):
        jet1group.add(Jet1(random.randint(SCREEN_WIDTH + 50, SCREEN_WIDTH * 4),
                           random.randint(50, 450), ally_x, ally_y))  # Jet spawned with coordinates and ally
        #  coordinates to target via ally_x and ally_y


def add_bomber_right(num_bombers, ally_x, ally_y):
    for _ in range(num_bombers):
        bomber_right_group.add(BomberRight(random.randint(SCREEN_WIDTH + 50, SCREEN_WIDTH * 3),
                                           random.randint(50, 550), ally_x, ally_y))


def add_bomber_left(num_bombers, ally_x, ally_y):
    for _ in range(num_bombers):
        bomber_left_group.add(BomberLeft(random.randint(- SCREEN_WIDTH * 2, -70),
                                         random.randint(50, 550), ally_x, ally_y))