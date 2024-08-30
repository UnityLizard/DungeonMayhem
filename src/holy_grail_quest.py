import random

from character import *
from level_setup import Level
from character_setup import *
from bag import *

#game variables
level = Level()
level.setup_level(1)
knights = knights_setup(["robin", "galahad", "lancelot", "bedevere", "king_arthur"])
enemies = enemies_setup(level.enemies)
bag = Bag(3, 5, 1)

action_cooldown = 0
action_wait_time = 12
ability_selected = None
item_selected = None
target = None
is_clicked = False
is_new_action = False
has_taken_action = False

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

    if isinstance(curr_character, Knight):
        if not bag.is_opened():
            curr_character.draw_abilities()
        bag.draw()

        if bag.is_opened() and back_button.is_clicked() and is_new_action:
            is_new_action = False
            bag.close()
        elif not bag.is_opened() and bag_button.is_clicked() and is_new_action:
            is_new_action = False
            bag.open()

        for ability in curr_character.abilities:
            if ability.is_activated() and not ability.is_on_cd() and not bag.is_opened():
                ability_selected = ability
                item_selected = None

        if bag.is_opened() and attack_potion_button.is_clicked() and bag.get_att_pot_cnt() != 0:
            ability_selected = None
            item_selected = "attack_potion"
        elif bag.is_opened() and heal_potion_button.is_clicked() and bag.get_heal_pot_cnt() != 0:
            ability_selected = None
            item_selected = "heal_potion"
        elif bag.is_opened() and invincibility_potion_button.is_clicked() and bag.get_inv_pot_cnt() != 0:
            ability_selected = None
            item_selected = "invincibility_potion"

        if ability_selected and ability_selected.get_type() == AbilityType.OFFENCE:
            pos = pygame.mouse.get_pos()
            for enemy in enemies:
                if enemy.rect.collidepoint(pos) and is_clicked:
                    target = enemy

        if ability_selected and ability_selected.get_type() == AbilityType.DEFENCE:
            pos = pygame.mouse.get_pos()
            for knight in knights:
                if knight.rect.collidepoint(pos) and is_clicked:
                    target = knight

        if ability_selected and ability_selected.get_type() == AbilityType.UTILITY:
            pos = pygame.mouse.get_pos()
            if curr_character.rect.collidepoint(pos) and is_clicked:
                target = curr_character

        if item_selected:
            pos = pygame.mouse.get_pos()
            if curr_character.rect.collidepoint(pos) and is_clicked:
                target = curr_character

    # attack action
    action_cooldown += 1
    if action_cooldown >= action_wait_time:
        died = []
        if isinstance(curr_character, Knight):
            if curr_character.stunned():
                has_taken_action = True
                curr_character.pass_turn()
            elif ability_selected and target:
                if ability_selected.get_name() == "normal_attack":
                    if curr_character.attack(target, 1):
                        died.append(target)
                elif ability_selected.get_name() == "multi_attack":
                    for enemy in enemies:
                        if curr_character.attack(enemy, 0.4):
                            died.append(enemy)
                elif ability_selected.get_name() == "stun":
                    curr_character.stun(target)
                    if curr_character.attack(target, 0.2):
                        died.append(target)
                elif ability_selected.get_name() == "heal":
                    curr_character.heal(target, 1)
                elif ability_selected.get_name() == "multi_heal":
                    for knight in knights:
                        curr_character.heal(knight, 0.4)
                elif ability_selected.get_name() == "taunt":
                    curr_character.taunt()
                elif ability_selected.get_name() == "dodge":
                    curr_character.dodge()
                has_taken_action = True
                ability_selected.set_on_cd()
                curr_character.pass_turn()
            elif item_selected and target:
                if item_selected == "attack_potion":
                    bag.use_att_pot()
                elif item_selected == "heal_potion":
                    bag.use_heal_pot()
                    curr_character.heal_pot()
                elif item_selected == "invincibility_potion":
                    bag.use_inv_pot()
                has_taken_action = True
                curr_character.pass_turn()
        else:
            if curr_character.stunned():
                has_taken_action = True
                curr_character.pass_turn()
            else:
                enemy_target = None
                for knight in knights:
                    if knight.is_taunting():
                        enemy_target = knight
                        break
                if not enemy_target:
                    enemy_target = random.choice(knights)
                if curr_character.attack(enemy_target, 1):
                    died.append(enemy_target)
                has_taken_action = True
                curr_character.pass_turn()
        
        for character in died:
            turn_order.remove(character)
            if isinstance(character, Knight):
                knights.remove(character)
            else:
                enemies.remove(character)
        action_cooldown = 0
        

    if has_taken_action:
        turn_order.append(curr_character)
        curr_character = None
        ability_selected = None
        item_selected = None
        target = None
        is_clicked = False
        has_taken_action = False
        bag.close()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_clicked = True
        else:
            is_clicked = False
        if event.type == pygame.MOUSEBUTTONUP:  
            is_new_action = True
    
    if not knights:
        is_running = False
        
    if not enemies:
        if level.curr_level == 5:
            is_win = True
            is_running = False
        else:
            level.curr_level += 1
            level.setup_level(level.curr_level)
            enemies = enemies_setup(level.enemies)
            turn_order = turn_order + enemies
            random.shuffle(turn_order)

    pygame.display.update()

pygame.quit()