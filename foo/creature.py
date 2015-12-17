import time

import pygame

import utilities


class Creature(pygame.sprite.Sprite):

    def __init__(self, surface, location):
        super().__init__()
        self.image = pygame.image.load("assets/images/cell.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.screen = pygame.display.get_surface()
        self.surface = surface

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 12
        if key[pygame.K_RIGHT] and self.rect.x < self.screen.get_size()[0] - 50:
            self.rect.x += dist
        elif key[pygame.K_LEFT] and self.rect.x > 10:
            self.rect.x -= dist
        elif key[pygame.K_UP] and self.rect.y > 8:
            self.rect.y -= dist
        elif key[pygame.K_DOWN] and self.rect.y < self.screen.get_size()[1] - 55:
            self.rect.y += dist
        elif key[pygame.K_e]:
            self.eat()
            
    def draw(self):
        """ Draw on surface """
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def eat(self):
        print("eating")
        # time.sleep(100)


class Food(pygame.sprite.Sprite):
    
    def __init__(self, surface, location):
        super().__init__()
        self.image = pygame.image.load("assets/images/food.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.surface = surface
        
    def draw(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))