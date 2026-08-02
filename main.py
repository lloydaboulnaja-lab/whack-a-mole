import pygame, sys
from pygame.locals import *


pygame.init() 

WIDTH, HEIGHT = 800, 600 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Whack A Mole!")

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.draw.rect(WIN, (20,140,97), pygame.Rect(70,70,70,70))

    pygame.display.flip()


