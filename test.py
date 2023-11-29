import pygame
import math

pygame.init()

#define screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Objects")

#define colours
BG = (255, 255, 255)
BLACK = (0, 0, 0)

turret_original = pygame.image.load("../convoydefense/assets/turret.jpg").convert_alpha()
x = 500
y = 300

#game loop
run = True
while run:

  #update background
  screen.fill(BLACK)

  pos = pygame.mouse.get_pos()
  x_dist = pos[0] - TURRET_X
  y_dist = -(pos[1] - TURRETY)
  angle = math.degrees(math.atan2(y_dist, x_dist))
  turret = pygame.transform.rotate(turret_original, angle - 90)
  turret_rect = turret.get_rect(center = (TURRET_X, TURRET_Y))

  SCREEN.blit(turret, turret_rect)

  #event handler
  for event in pygame.event.get():
    #quit program
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()