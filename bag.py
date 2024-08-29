import button

from general_info import *

bag_button = button.Button(screen, 515, screen_height - bottom_panel + 105, img_bag, 470, 80)
back_button = button.Button(screen, 515, screen_height - bottom_panel + 105, img_back, 470, 80)

attack_potion_button = button.Button(screen, 15, screen_height - bottom_panel + 15, img_attack_potion, 380, 80)
heal_potion_button = button.Button(screen, 15, screen_height - bottom_panel + 105, img_heal_potion, 380, 80)
invincibility_potion_button = button.Button(screen, 515, screen_height - bottom_panel + 15, img_invincibility_potion, 380, 80)

image_cnt_1 = pygame.transform.scale(img_cd_1, (80, 80))
image_cnt_2 = pygame.transform.scale(img_cd_2, (80, 80))
image_cnt_3 = pygame.transform.scale(img_cd_3, (80, 80))
image_cnt_4 = pygame.transform.scale(img_cd_4, (80, 80))
image_cnt_5 = pygame.transform.scale(img_cd_5, (80, 80))

#bag class
class Bag():
    def __init__(self, att_pot_cnt, heal_pot_cnt, inv_pot_cnt):
        self.bIsOpen = False
        self.att_pot_cnt = att_pot_cnt
        self.heal_pot_cnt = heal_pot_cnt
        self.inv_pot_cnt = inv_pot_cnt

    def is_open(self):
        return self.bIsOpen

    def open(self):
        self.bIsOpen = True

    def close(self):
        self.bIsOpen = False

    def use_att_pot(self):
        self.att_pot_cnt -= 1

    def use_heal_pot(self):
        self.heal_pot_cnt -= 1

    def use_inv_pot(self):
        self.inv_pot_cnt -= 1

    def draw(self):
        if (self.bIsOpen):
            back_button.draw()
            if (self.att_pot_cnt):
                attack_potion_button.draw()
                screen.blit(eval(f'image_cnt_{self.att_pot_cnt}'), (405, screen_height - bottom_panel + 15))
            if (self.heal_pot_cnt):
                heal_potion_button.draw()
                screen.blit(eval(f'image_cnt_{self.heal_pot_cnt}'), (405, screen_height - bottom_panel + 105))
            if (self.inv_pot_cnt):
                invincibility_potion_button.draw()
                screen.blit(eval(f'image_cnt_{self.inv_pot_cnt}'), (905, screen_height - bottom_panel + 15))
        else:
            bag_button.draw()
        
        