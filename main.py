import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
bottom_panel = 200
screen_width = 1000
screen_height = 500 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Holy Grail Quest')

#load images
#background image
img_level1 = pygame.image.load('img/background/level2.png').convert_alpha()
#panel image
img_panel = pygame.image.load('img/panel/panel.png').convert_alpha()

#drawing background
def draw_bg():
    screen.blit(img_level1, (0, 0))

#drawing panel
def draw_panel():
    screen.blit(img_panel, (0, screen_height - bottom_panel))

#fighter class
class Fighter():
	def __init__(self, x, y, name, max_hp, strength, potions):
		self.name = name
		self.max_hp = max_hp
		self.hp = max_hp
		self.strength = strength
		self.alive = True
		self.image = pygame.image.load(f'img/characters/{self.name}.png')
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)


	def draw(self):
		screen.blit(self.image, self.rect)
            
knight1 = Fighter(350, 360, 'king_arthur', 0, 0, 0)
knight2 = Fighter(280, 360, 'bedevere', 0, 0, 0)
knight3 = Fighter(210, 360, 'lancelot', 0, 0, 0)
knight4 = Fighter(140, 360, 'galahad', 0, 0, 0)
knight5 = Fighter(70, 360, 'robin', 0, 0, 0)

enemy1 = Fighter(420, 360, 'french', 0, 0, 0)
enemy2 = Fighter(490, 360, 'ni_knight_small', 0, 0, 0)
enemy3 = Fighter(560, 360, 'ni_knight_big', 0, 0, 0)
enemy4 = Fighter(630, 360, 'three_headed_knight', 0, 0, 0)
enemy5 = Fighter(700, 385, 'tim_enchanter', 0, 0, 0)
enemy6 = Fighter(820, 375, 'black_knight', 0, 0, 0)
enemy7 = Fighter(700, 300, 'killer_rabbit', 0, 0, 0)
enemy8 = Fighter(420, 360, 'black_beast', 0, 0, 0)

run = True
while run:

    clock.tick(fps)

    draw_bg()
    draw_panel()

    knight1.draw()
    knight2.draw()
    knight3.draw()
    knight4.draw()
    knight5.draw()

    enemy1.draw()
    enemy2.draw()
    enemy3.draw()
    enemy4.draw()
    enemy5.draw()
    enemy6.draw()
    enemy7.draw()
    enemy8.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()