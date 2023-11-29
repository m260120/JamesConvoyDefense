
from gameparameters import *
from math import atan2, degrees


class Player:
    def __init__(self):
        # super().__init__()
        self.image = pygame.image.load("./assets/turret.jpg").convert()
        self.image_og_size = self.image.get_size()  # Resizing base, returns a tuple
        self.image_new_size = (self.image_og_size[0] * .15, self.image_og_size[1] * .15)
        self.image = pygame.transform.scale(self.image, self.image_new_size)
        self.image = pygame.transform.rotate(self.image, 90)

        self.image.set_colorkey((255, 255, 255))
        self.image_rect = self.image.get_rect()

        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2

        self.turret_rect = self.image.get_rect(center=(self.x, self.y))

        self.angle = 0

    def update(self, screen):
        pos = pygame.mouse.get_pos()  # Track mouse

        x_dist = pos[0] - self.x  # Calculate legs of triangle to get theta
        y_dist = - (pos[1] - self.y)
        self.angle = degrees(atan2(y_dist, x_dist))  # Calculate theta

        turret = pygame.transform.rotate(self.image, self.angle - 90)  # Rotate the turret to the angle,
        # also accounting for offset of the image. Must assign new rotated image as a new variable
        # "turret." Or else there will be an overload

        turret_rect = turret.get_rect(center=(self.x, self.y))  # Assign the center of the new turret
        # a value that it will not deviate from so the turret stays in place

        screen.blit(turret, turret_rect)  # With these new parameters on the rectangle in place,
        # redraw the rectangle

        # Infinite loop in the game file will constantly update the turret by assigning a new
        # rectangle, "Turret" each time

