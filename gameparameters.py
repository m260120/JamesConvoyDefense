
import pygame

pygame.init()

# Screen Dimensions
TILE_SIZE = 64
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600

# Asset Speeds
JET1_SPEED = 2  # 6
JET2_SPEED = 4  # 11
BOMBER_SPEED = 1  # 4
BULLET_SPEED = 25

# Sounds
shoot = pygame.mixer.Sound("./sounds/firing.mp3")
jet1_hit = pygame.mixer.Sound("./sounds/jet1_hit.wav")
jet2_hit = pygame.mixer.Sound("./sounds/jet2_hit.wav")
bomber_hit = pygame.mixer.Sound("./sounds/bomber_hit.wav")
ally_hit = pygame.mixer.Sound("./sounds/vineboom.mp3")
power_up = pygame.mixer.Sound("./sounds/powerup.wav")
