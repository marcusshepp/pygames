import pygame


class Creature:

    def __init__(self, screen, color, location):
        self.location = location
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.location, 50)
