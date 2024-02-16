import copy
from general_info import *

#information about enemies per level
level_info = []
level_info.append(['french', 'french', 'french', 'french', 'french']) # level 1
level_info.append(['ni_knight_small', 'ni_knight_small', 'ni_knight_small', 'ni_knight_big']) # level 2
level_info.append(['black_knight', 'tim_enchanter']) # level 3
level_info.append(['three_headed_knight', 'killer_rabbit']) # level 4
level_info.append(['black_beast']) # level 5


class Level():
	def __init__(self):
		self.level = 1
		self.background = pygame.image.load(f'img/background/level{1}.png')
		self.enemies = copy.deepcopy(level_info[0])
		
    #getting level info
	def setup_level(self, level):
		self.background = pygame.image.load(f'img/characters/{level}.png')
		self.enemies = copy.deepcopy(level_info[level - 1])
		
    #drawing background
	def draw_bg(self):
		screen.blit(self.background, (0, 0))
