import random

from general_info import *

#fighter class
class Character():
	def __init__(self, x, y, name, max_hp, strength):
		self.name = name
		self.max_hp = max_hp
		self.hp = max_hp
		self.strength = strength
		self.alive = True
		self.position = (x, y)
		self.image = pygame.image.load(f'img/characters/{self.name}.png')
		self.rect = self.image.get_rect(bottomleft = self.position)

	def attack(self, target):
		#deal damage to enemy
		rand = random.randint(-5, 5)
		damage = self.strength + rand
		target.hp -= damage
		#check if target has died
		if target.hp < 1:
			target.hp = 0
			target.alive = False
			return True
		return False

	def draw(self):
		screen.blit(self.image, self.rect)
		self._draw_health_bar()

	def _draw_health_bar(self):
		#calculate health ratio
		ratio = self.hp / self.max_hp
		#calculate posotion
		x = self.position[0]
		y = self.position[1]

		pygame.draw.rect(screen, red, (x, y, self.rect.width, 20))
		pygame.draw.rect(screen, green, (x, y, self.rect.width * ratio, 20))
		draw_text(f'{self.hp}/{self.max_hp}', font, black, x + self.rect.width / 2, y + 10)
