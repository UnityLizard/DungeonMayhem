import copy

from character import *
from level_setup import Level
from character_setup import *

#game variables
level = Level()
knights = characters_setup(["robin", "galahad", "lancelot", "bedevere", "king_arthur"], True)
enemies = characters_setup(level.enemies, False)

run = True
while run:

    clock.tick(fps)

    level.draw_bg()
    draw_panel()

    for knight in knights:
        knight.draw()
        
    for enemy in enemies:
        enemy.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()