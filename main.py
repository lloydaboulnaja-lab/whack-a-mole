import pygame, sys
from pygame.locals import *

pygame.init() 

WIDTH, HEIGHT = 900, 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Whack A Mole!")

grass = (34, 139, 34)

running = True

text_font = pygame.font.SysFont("Arial", 40, bold=True)

FPS = 60

def draw(text, font, color, x, y,):
    img = font.render(text,True, color)
    WIN.blit(img, (x, y))

while running:

    WIN.fill(grass)

    frames = pygame.time.Clock()

    frames.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            print("Mouse has been clicked!")

    a = pygame.draw.rect(WIN, (12,21,71), pygame.Rect((20,40,400,300)))

    
    pygame.draw.circle(WIN, (131, 101, 57), (190,230), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190+250,230), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190+250+250,230), 49)

    pygame.draw.circle(WIN, (131, 101, 57), (190,230+250), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190+250,230+250), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190+250+250,230+250), 49)
    

    draw("SCORE",text_font, (12,98,205), 20, 20)
   
    pygame.display.flip()

