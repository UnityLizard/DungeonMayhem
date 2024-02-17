import random
import time

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
is_attack_selected = False
is_clicked = False
has_taken_action = False
target = None

#works like queue to track order
turn_order = knights + enemies
random.shuffle(turn_order)
curr_character = None

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


    if not curr_character:
        curr_character = turn_order.pop(0)

    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()

    for enemy in enemies:
        if enemy.rect.collidepoint(pos):
            #hide mouse
            pygame.mouse.set_visible(False)
			#show sword in place of mouse cursor
            screen.blit(img_sword, pos)
            if is_clicked:
                is_attack_selected = True
                target = enemy

    #attack action
    action_cooldown += 1
    if action_cooldown >= action_wait_time:
        if curr_character in knights:
            if is_attack_selected and target:
                if curr_character.attack(target):
                    turn_order.remove(target)
                    enemies.remove(target)
                target = None
                has_taken_action = True
        else:
            enemy_target =  random.choice(knights)
            if curr_character.attack(enemy_target):
                turn_order.remove(enemy_target)
                knights.remove(enemy_target)
            has_taken_action = True
        action_cooldown = 0
        

    if has_taken_action:
        turn_order.append(curr_character)
        curr_character = None
        has_taken_action = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_clicked = True
        else:  
            is_clicked = False
    
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
            turn_order = turn_order + enemies
            random.shuffle(turn_order)

    pygame.display.update()

pygame.quit()