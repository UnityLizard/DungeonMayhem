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

#define fonts
font = pygame.font.SysFont('Comic Sans', 12)

#define colours
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

#drawing text
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.center = (x, y)
    screen.blit(surface, rect)

#panel image
img_panel = pygame.image.load('img/panel/panel.png').convert_alpha()

#buttons images
img_def_attack = pygame.image.load('img/icons/attack.png').convert_alpha()
img_multi_attack = pygame.image.load('img/icons/multi_attack.png').convert_alpha()
img_stun_attack = pygame.image.load('img/icons/stun.png').convert_alpha()
img_heal = pygame.image.load('img/icons/heal.png').convert_alpha()
img_multi_heal = pygame.image.load('img/icons/multi_heal.png').convert_alpha()
img_taunt = pygame.image.load('img/icons/taunt.png').convert_alpha()
img_dodge = pygame.image.load('img/icons/dodge.png').convert_alpha()
img_bag = pygame.image.load('img/icons/bag.png').convert_alpha()
img_attack_potion = pygame.image.load('img/icons/attack_potion.png').convert_alpha()
img_heal_potion = pygame.image.load('img/icons/heal_potion.png').convert_alpha()
img_invincibility_potion = pygame.image.load('img/icons/invincibility_potion.png').convert_alpha()
img_back = pygame.image.load('img/icons/back.png').convert_alpha()
img_cd_none = pygame.image.load('img/icons/cd_none.png').convert_alpha()
img_cd_0 = pygame.image.load('img/icons/cd_0.png').convert_alpha()
img_cd_1 = pygame.image.load('img/icons/cd_1.png').convert_alpha()
img_cd_2 = pygame.image.load('img/icons/cd_2.png').convert_alpha()
img_cd_3 = pygame.image.load('img/icons/cd_3.png').convert_alpha()
img_cd_4 = pygame.image.load('img/icons/cd_4.png').convert_alpha()
img_cd_5 = pygame.image.load('img/icons/cd_5.png').convert_alpha()

#drawing panel
def draw_panel():
    screen.blit(img_panel, (0, screen_height - bottom_panel))