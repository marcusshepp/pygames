import pygame

import utilities
import creature


pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
c0 = creature.Creature(screen, (0, 0, 255), (500, 500))
c0.draw()

BLACK = (0, 0, 0)

info = pygame.display.Info()
sw = info.current_w
sh = info.current_h

# initial position
x = y = 0
# initial direction
dx = 5
dy = 2


running = True
while running:
    running = utilities.check_for_quit()
    # update position with direction
    x += dx
    y += dy

    # check bounds
    if x - dx < 0 or x + dx > sw:
        dx = -dx
    if y - dy < 0 or y + dy > sh:
        dy = -dy

    screen.fill(BLACK)
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

#
# running = True
# while running:
#     running = utilities.check_for_quit()
#     c0.update()
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()
