import pygame


class Creature(pygame.sprite.Sprite):

    def __init__(self, screen, color, location):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.location = list(location)
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.location, 10)

    def update(self):
        nxt = next(self.next_move())
        for i, v in enumerate(self.location):
            self.location[i] += nxt[i]
        pygame.draw.circle(self.screen, self.color, self.location, 10)
    
    def next_move(self):
        screen_size = self.screen.get_size()
        next_location = list()
        if self.location[0] < screen_size[0]:
            if self.location[1] < screen_size[1]:
                yield (1, 1)
        