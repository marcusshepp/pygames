import pygame

from .utils import (
    BLACK,
    WHITE)


class Galaga(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/galaga.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 550

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 12
        if key[pygame.K_RIGHT]:
            self.rect.x += dist
        elif key[pygame.K_LEFT]:
            self.rect.x -= dist

    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def reset_position(self):
        self.rect.x = 350
        self.rect.y = 550


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self, origin):
        super().__init__()
        self.image = pygame.image.load("assets/images/galaga_bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = origin.rect.x
        self.rect.y = origin.rect.y

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 12


class Enemy1(pygame.sprite.Sprite):

    def __init__(self, originy):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy1.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.originx = 0
        self.originy = originy
        self.left = False
        self.rect.y = originy
        self.attack = False

    def update(self):
        """ move left - right """
        if self.left:
            self.rect.x -= 1
        else:
            self.rect.x += 1
        if abs(self.rect.x - self.originx) == 150:
            # if i've moved 150 px to the left
            self.left = True
        elif abs(self.rect.x - self.originx) == 0:
            # if I'm in the same position I was instantiated at.
            self.left = False

    def make_attack(self):
        """ attack the player aka galaga """
        if self.rect.y < 600:
            self.rect.y += 5
        else: self.rect.y = self.originy
        

class Enemy2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy2.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = 35
        self.originx = 0
        self.originy = 0
        self.left = False
        self.attack = False

    def update(self):
        """ Moving back and fourth through space """
        if self.left:
            self.rect.x -= 2
        else:
            self.rect.x += 2
        if abs(self.rect.x - self.originx) == 150:
            self.left = True
        elif abs(self.rect.x - self.originx) == 0:
            self.left = False

    def make_attack(self):
        """ attack the player aka galaga """
        pass


class Life(Galaga):

    def __init__(self, x, y):
        super().__init__()
        self.rect.x = x
        self.rect.y = y

