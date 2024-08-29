import button

from general_info import *

#ablity class
class Ability():
    def __init__(self, name, cd, x, y, img, width, height):
        self.name = name
        self.curr_cd = 0
        self.max_cd = cd
        self.ability_button = button.Button(screen, x, screen_height - bottom_panel + y, img, width, height)
        self.cd_buttons = []
        if cd == 0:
            self.cd_buttons.append(button.Button(screen, width + x + 10, screen_height - bottom_panel + y, img_cd_none, height, height))
        else:
             for i in range(cd - 1):
                 self.cd_buttons.append(button.Button(screen, width + x + 10, screen_height - bottom_panel + y, eval(f'img_cd_{i}'), height, height))

    def draw(self):
        self.ability_button.draw()
        self.cd_buttons[self.curr_cd].draw()

    def activate(self):
        self.cd = self.max_cd
        return self.name
        