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

run = True
while run:

    clock.tick(fps)

    draw_bg()
    draw_panel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()