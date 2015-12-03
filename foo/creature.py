import pygame


class Creature(pygame.sprite.Sprite):

    def __init__(self, screen, color, location):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.location = location
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.location, 10)

    def update(self):
        self.area.x += 1
        self.area.y += 1