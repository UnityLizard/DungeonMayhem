import pygame 

#button class
class Button():
	def __init__(self, surface, x, y, image, size_x, size_y):
		self.image = pygame.transform.scale(image, (size_x, size_y))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.surface = surface

	def draw(self):
		self.surface.blit(self.image, (self.rect.x, self.rect.y))

	def is_clicked(self):
		pos = pygame.mouse.get_pos()
		return self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1
