import random

import pygame

from galaga.sprites import (
    Galaga,
    Enemy1,
    Enemy2,
    Life,
    Bullet)
from galaga.utils import (
    BLACK,
    WHITE)
    
pygame.init()
score = 0
running = True
clock = pygame.time.Clock()
size = (800, 600)
screen = pygame.display.set_mode(size)

# caption and mouse
pygame.display.set_caption("Galaga")
# pygame.mouse.set_visible(False)
pygame.font.init()
font_path = "assets/fonts/arcade.ttf"
fontobj = pygame.font.Font(font_path, 32)

# sprite lists
e_list = pygame.sprite.Group()
enemies = []
all_sprites_list = pygame.sprite.Group()

# create player
player = Galaga()
bullet_list = pygame.sprite.Group()

# create enemies
positions = [i for i in range(50, 750, 100)]
for i in range(6):
    e = Enemy1(originy=0)
    e.rect.x = positions[i]
    e.originx = e.rect.x
    e_list.add(e)
    all_sprites_list.add(e)
    enemies.append(e)
positions = [i for i in range(80, 750, 125)]
for i in range(5):
    e = Enemy2()
    e.rect.x = positions[i]
    e.originx = e.rect.x
    e_list.add(e)
    all_sprites_list.add(e)
    enemies.append(e)
positions = [i for i in range(50, 750, 100)]
for i in range(6):
    e = Enemy1(originy=70)
    e.rect.x = positions[i]
    e.originx = e.rect.x
    e_list.add(e)
    all_sprites_list.add(e)
    enemies.append(e)

rand_enemy_one = random.randrange(0, 4)
rand_enemy_two = random.randrange(5, 10)

# create lives
lives = pygame.sprite.Group()
lives_index = 0
life1 = Life(650, 550)
life2 = Life(700, 550)
life3 = Life(750, 550)
lives.add(life1)
lives.add(life2)
lives.add(life3)
all_sprites_list.add(life1)
all_sprites_list.add(life2)
all_sprites_list.add(life3)
# print(help(pygame.draw.rect))

def draw_box(surface, boxx, boxy, color, width, height):
    """
    in: pygame surface, x coor, y coor, width, height of box
    out: void
    Draws a box
    """
    pygame.draw.rect(surface, color, (boxx, boxy, width, height))

def mouse_over(mx,my,x,y,w,h):
    """
    in: mouse x, y coor, box x, y coor, width, height of box
    out: is the mouse in the box?
    """
    if x+w > mx > x and y+h > my > y:
        return True

def is_finished(event):
    return True if event.type == pygame.QUIT else False

def start_screen():
    """
    First function to be called.
    Beginning of the game.
    """
    finished = False
    while not finished:
        for event in pygame.event.get():
            finished = is_finished(event)
        screen.fill(BLACK)
        label = fontobj.render("GALAGA", 1, (255, 255, 0))
        screen.blit(label, (350, 50))
        start_button = fontobj.render("Start Button", 1, (255, 255, 0))
        screen.blit(start_button, (300, 300))
        mouse_coordinates = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        # draw_box(screen, 300, 300, BLACK, 255, 255)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_over(mouse_x, mouse_y, 300, 300, 255, 55) and any(clicked):
            return
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

def end_screen():
    """
    Last function to be called.
    End of the game.
    """
    finished = False
    while not finished:
        for event in pygame.event.get():
            finished = is_finished(event)
            if event.type == pygame.KEYDOWN:
                finished = True
        screen.fill(BLACK)
        label = fontobj.render("GAME OVER", 1, (255, 255, 0))
        screen.blit(label, (300, 200))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

start_screen()
attacking_enemies = []

while running:
    for event in pygame.event.get():
        finished = is_finished(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                if len(bullet_list) <= 1:
                    info = {"origin": player}
                    bullet = Bullet(**info)
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

    screen.fill(BLACK)
    player.draw(screen)
    player.handle_keys()
    all_sprites_list.draw(screen)
    all_sprites_list.update()

    # win
    if not len(e_list):
        end_screen()
    # dead
    if pygame.sprite.spritecollide(player, e_list, True):
        if lives_index == 0:
            life1.kill()
        elif lives_index == 1:
            life2.kill()
        elif lives_index == 2:
            life3.kill()
        lives_index += 1
        player.reset_position()
    # no more enemies
    if len(attacking_enemies) == 0:
        attacking_enemies.append(enemies[rand_enemy_one])
        attacking_enemies.append(enemies[rand_enemy_two])
    
    enemies[rand_enemy_one].make_attack()
    enemies[rand_enemy_two].make_attack()

    # get rid of bullets and collid with enemies
    for bullet in bullet_list:
        enemies_hit_list = pygame.sprite.spritecollide(bullet, e_list, True)
        for enemy in enemies_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    label = fontobj.render("Score: {0}".format(score), 1, (255, 255, 0))
    screen.blit(label, (30, 560))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
