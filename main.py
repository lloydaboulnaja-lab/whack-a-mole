import pygame
import time
import random




pygame.init()
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BG = pygame.image.load("background.jpeg")
pygame.display.set_caption("Whackk a mole!")
pygame.display.set_icon(WIN) 

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

def draw():
    WIN.blit(BG, (0,0))
    pygame.display.update()


def main():
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        draw()
    pygame.quit()


if __name__ == "__main__":
    main()
