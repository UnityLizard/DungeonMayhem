import random
import math

from general_info import *

#character class
class Character():
	def __init__(self, x, y, name, max_hp, strength):
		self.name = name
		self.max_hp = max_hp
		self.hp = max_hp
		self.ratio = 1
		self.ratio_duration = 0
		self.strength = strength
		self.is_stunned = False
		self.has_taunt = False
		self.taunt_duration = 0
		self.has_dodge = False
		self.dodge_duration = 0
		self.has_invincibility = False
		self.invincibility_duration = 0
		self.alive = True
		self.position = (x, y)
		self.image = pygame.image.load(f'img/characters/{self.name}.png')
		self.rect = self.image.get_rect(bottomleft = self.position)

	def attack(self, target, ratio):
		#deal damage to enemy
		rand = random.randint(-5, 5)
		damage = self.ratio * math.floor(ratio * (self.strength + rand))
		#dodge is 50% to miss the attack and invincibility is 100%
		if target.has_invincibility:
			return False
		if target.has_dodge and random.randint(0, 1):
			return False
		target.hp -= damage
		#check if target has died
		if target.hp < 1:
			target.hp = 0
			target.alive = False
			return True
		return False

	def heal(self, target, ratio):
		#heal amount
		rand = random.randint(0, 5)
		heal_amount = math.ceil(2 * ratio * (self.strength + rand))
		target.hp += heal_amount
		target.hp = min(target.hp, target.max_hp)

	def stun(self, target):
		target.is_stunned = True

	def taunt(self):
		self.has_taunt = True
		self.taunt_duration = 2

	def dodge(self):
		self.has_dodge = True
		self.dodge_duration = 3

	def invincibility(self):
		self.has_invincibility = True
		self.invincibility_duration = 4

	def increase_ratio(self):
		self.ratio = self.ratio + 1
		self.ratio_duration = 4

	def is_taunting(self):
		return self.has_taunt

	def stunned(self):
		return self.is_stunned

	def pass_turn(self):
		self.is_stunned = False
		
		self.taunt_duration = max(0, self.taunt_duration - 1)
		if not self.taunt_duration:
			self.has_taunt = False

		self.dodge_duration = max(0, self.dodge_duration - 1)
		if not self.dodge_duration:
			self.has_dodge = False

		self.invincibility_duration = max(0, self.invincibility_duration - 1)
		if not self.invincibility_duration:
			self.has_invincibility = False

		self.ratio_duration = max(0, self.ratio_duration - 1)
		if not self.ratio_duration:
			self.ratio = 1

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
