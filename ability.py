import button

from general_info import *

#create buttons
# attack_def_button = button.Button(screen, 10, screen_height - bottom_panel + 10, img_def_attack, 400, 80)
# attack_potion_button = button.Button(screen, 10, screen_height - bottom_panel + 10, img_attack_potion, 400, 80)

# attack_multi_button = button.Button(screen, 10, screen_height - bottom_panel + 110, img_multi_attack, 400, 80)
# heal_button = button.Button(screen, 10, screen_height - bottom_panel + 110, img_heal, 400, 80)
# taunt_button = button.Button(screen, 10, screen_height - bottom_panel + 110, img_taunt, 400, 80)
# heal_potion_button = button.Button(screen, 10, screen_height - bottom_panel + 110, img_heal_potion, 400, 80)

# attack_stun_button = button.Button(screen, 510, screen_height - bottom_panel + 10, img_stun_attack, 400, 80)
# heal_multi_button = button.Button(screen, 510, screen_height - bottom_panel + 10, img_multi_heal, 400, 80)
# dodge_button = button.Button(screen, 510, screen_height - bottom_panel + 10, img_dodge, 400, 80)
# invincibility_potion_button = button.Button(screen, 510, screen_height - bottom_panel + 10, img_invincibility_potion, 400, 80)

# bag_button = button.Button(screen, 510, screen_height - bottom_panel + 110, img_bag, 400, 80)
# back_button = button.Button(screen, 510, screen_height - bottom_panel + 110, img_back, 400, 80)

#ablity class
class Ability():
    def __init__(self, name, cd, x, y, img, width, height):
        self.name = name
        self.curr_cd = 0
        self.max_cd = cd
        self.attack_button = button.Button(screen, x, screen_height - bottom_panel + y, img, width, height)
        # self.cd_buttons = []
        # if cd == 0:
        #     self.cd_buttons.append(button.Button(screen, width + x, screen_height - bottom_panel + y, img_cd_none, height, height))
        # else:
        #     for i in range(cd):
        #         self.cd_buttons.append(button.Button(screen, width + x, screen_height - bottom_panel + y, f'img_cd_{i}', height, height))

    def draw(self):
        self.attack_button.draw()
        # self.cd_buttons[self.cd].draw()

    def activate(self):
        self.cd = self.max_cd
        return self.name
        