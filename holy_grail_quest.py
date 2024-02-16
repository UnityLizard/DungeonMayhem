import copy
import random

from character import *
from level_setup import Level
from character_setup import *

#game variables
level = Level()
level.setup_level(1)
knights = characters_setup(["robin", "galahad", "lancelot", "bedevere", "king_arthur"], True)
enemies = characters_setup(level.enemies, False)
action_cooldown = 0
action_wait_time = 10


turn_order = knights + enemies
random.shuffle(turn_order)

is_running = True
is_win = False

while is_running:

    clock.tick(fps)

    level.draw_bg()
    draw_panel()

    for knight in knights:
        knight.draw()
        
    for enemy in enemies:
        enemy.draw()

    curr_character = turn_order.pop(0)

    if curr_character in knights:
        action_cooldown += 1
        if action_cooldown >= action_wait_time:
            if curr_character.attack(enemies[0]):
                enemies.remove(enemies[0])
            action_cooldown = 0


    turn_order.append(curr_character)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    if not knights:
        is_running = False
        
    if not enemies:
        if level.curr_level == 5:
            is_win = True
            is_running = False
        else:
            level.curr_level += 1
            level.setup_level(level.curr_level)
            enemies = characters_setup(level.enemies, False)

    pygame.display.update()

pygame.quit()