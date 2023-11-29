import pygame.sprite


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        for i in range(1, 6):
            exp_image = pygame.image.load(f'./assets/explosion/exp{i}.png')
            exp_image = pygame.transform.scale(exp_image, (150, 150))  # Adding explosion frames to a list
            self.images.append(exp_image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        explosion_speed = 4  # How fast the animation updates
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:  # prevents index from returning
            #  an out-of-bounds error
            self.counter = 0  # reset counter
            self.index += 1  # increase index from zero
            self.image = self.images[self.index]  # access specific explosion sprite
    # reset index after explosion is done
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()  # this kills the instance of the explosion once it is done animating


explosions = pygame.sprite.Group()
