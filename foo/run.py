import pygame

import utilities
import creature


pygame.init()
size = (1000, 900)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
c0 = creature.Creature(screen, (100, 200))
f = creature.Food(screen, (300, 100))

running = True
while running:
    running = utilities.check_for_quit()
    screen.fill(utilities.BLACK)
    f.draw()
    c0.draw()
    c0.handle_keys()
    if c0.rect.colliderect(f.rect):
        print("EATING")
        f.remove()
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()
