import pygame, sys
from pygame.locals import *
import random


pygame.init() 

WIDTH, HEIGHT = 900, 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Whack A Mole!")

grass = (34, 139, 34)

text_font = pygame.font.SysFont("Arial", 40, bold=True)

FPS = 60

frames = pygame.time.Clock()

positions = [
(190, 230),
(440, 230),
(690, 230),(190, 480),
(440, 480),(690, 480)]

print(len(positions))

x,y = 20,40

a =  pygame.Rect(x,y,400,300)

def draw(text, font, color, x, y,):
    img = font.render(text,True, color)
    WIN.blit(img, (x, y))



class Mole:
    def __init__(self,mole_pos,mole_rect,appearance):
        self.mole_pos = mole_pos
        self.mole_rect = mole_rect
        self.appearance = appearance

    def draw_mole(self):
        return self.mole_rect
        pygame.draw.rect()

    def change_pos(self):
        return self.appearance
        pygame.draw.rect()
    




running = True

while running:

    frames.tick(FPS)

    WIN.fill(grass)
    
    pygame.draw.rect(WIN, (82,120,231), a)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:        
            print(f"The position is: {event.pos}!")

            flag_ = a.collidepoint(event.pos)

            if flag_ == True:
                rand_pos  = random.choice(positions)
                a.x, a.y = rand_pos
                print("HIT")
            else:
                print("MISS")

    

    
    
    pygame.draw.circle(WIN, (131, 101, 57), (190,230), 49)

    pygame.draw.circle(WIN, (57, 45, 43), (190,230), 32)
    pygame.draw.circle(WIN, (57, 45, 43), (165, 210), 10)  
    pygame.draw.circle(WIN, (57, 45, 43), (215, 210), 10)  
    pygame.draw.circle(WIN, (235, 150, 165), (165, 210), 5)  
    pygame.draw.circle(WIN, (235, 150, 165), (215, 210), 5)  
    pygame.draw.circle(WIN, (57, 45, 43), (190, 230), 32)
    pygame.draw.circle(WIN, (0, 0, 0), (178, 225), 3)  
    pygame.draw.circle(WIN, (0, 0, 0), (202, 225), 3)  
    pygame.draw.circle(WIN, (235, 150, 165), (190, 245), 6)
    pygame.draw.line(WIN, (0, 0, 0), (187, 252), (193, 252), 2)


    pygame.draw.circle(WIN, (131, 101, 57), (190+250,230), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190+250+250,230), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190,230+250), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190+250,230+250), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190+250+250,230+250), 49)
    

    draw("SCORE",text_font, (12,98,205), 20, 20)
   
    pygame.display.flip()
