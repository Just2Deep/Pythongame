import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
#icon = pygame.image.load('ufo.png')
#pygame.display.set_icon(icon)

# Game loop  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((192,192,192))
    pygame.display.update()

