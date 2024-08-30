import button

from general_info import *

#ablity class
class Ability():
    def __init__(self, name, cd, ability_type, x, y, img, width, height):
        self.name = name
        self.curr_cd = 0
        self.max_cd = cd
        self.type = ability_type
        self.ability_button = button.Button(screen, x, screen_height - bottom_panel + y, img, width, height)
        self.cd_buttons = []
        if cd == 0:
            self.cd_buttons.append(button.Button(screen, width + x + 10, screen_height - bottom_panel + y, img_cd_none, height, height))
        else:
             for i in range(cd + 1):
                 self.cd_buttons.append(button.Button(screen, width + x + 10, screen_height - bottom_panel + y, eval(f'img_cd_{i}'), height, height))

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def is_activated(self):
        return self.ability_button.is_clicked()

    def is_on_cd(self):
        return self.curr_cd != 0

    def set_on_cd(self):
        self.curr_cd = self.max_cd
        return self.name

    def reduce_cd(self):
        self.curr_cd = max(0, self.curr_cd - 1)

    def draw(self):
        self.ability_button.draw()
        self.cd_buttons[self.curr_cd].draw()
        