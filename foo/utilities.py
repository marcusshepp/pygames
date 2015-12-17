import pygame


def check_for_quit():
    """ Checks for quit keys """
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            return False
        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_ESCAPE:
                return False
    return True
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
