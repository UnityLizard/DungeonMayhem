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

#drawing panel
def draw_panel():
    screen.blit(img_panel, (0, screen_height - bottom_panel))