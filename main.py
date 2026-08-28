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

    def __init__(self,pos):
        self.pos = pos


    




    def draw_mole(self,surface):
        self.surface = surface
        
       
        body = pygame.draw.circle(WIN, (57, 45, 43), self.pos, 32)
        left_ear = pygame.draw.circle(WIN, (57, 45, 43), (165, 210), 10)  
        right_ear = pygame.draw.circle(WIN, (57, 45, 43), (215, 210), 10)  
        left_pink = pygame.draw.circle(WIN, (235, 150, 165), (165, 210), 5)  
        right_pink = pygame.draw.circle(WIN, (235, 150, 165), (215, 210), 5)  
        left_eye = pygame.draw.circle(WIN, (0, 0, 0), (178, 225), 3)  
        right_eye = pygame.draw.circle(WIN, (0, 0, 0), (202, 225), 3)  
        nose = pygame.draw.circle(WIN, (235, 150, 165), (190, 245), 6)
        mouth = pygame.draw.line(WIN, (0, 0, 0), (187, 252), (193, 252), 2)
    
        


my_mole = Mole((440,230))
my_mole.change_characteristics()

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
    pygame.draw.circle(WIN, (131, 101, 57), (440,230), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (690,230), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (190,480), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (440,480), 49)
    pygame.draw.circle(WIN, (131, 101, 57), (690,480), 49)

    
    my_mole.draw_mole(WIN)



    draw("SCORE",text_font, (12,98,205), 20, 20)
   
    pygame.display.flip()
    
