import pygame

import utilities
import creature


pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
c0 = creature.Creature(screen, (0, 0, 255), (500, 500))
c0.draw()

running = True
while running:
    running = utilities.check_for_quit()
    c0.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
