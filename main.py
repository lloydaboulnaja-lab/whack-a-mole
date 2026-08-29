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

mole_rect_pos = [
(190-25, 230-35),
(440-25, 230-35),
(690-25, 230-35),(190-25, 480-35),
(440-25, 480-35),(690-25, 480-35)]

rand_pos  = random.choice(positions)


def draw(text, font, color, x, y,):
    img = font.render(text,True, color)
    WIN.blit(img, (x, y))



class Mole:

    def __init__(self,pos):
        
        self.pos = pos
        x,y = self.pos

        

        self.mole_rect = pygame.Rect(x-25,y-35,64,64)
           

    def draw_mole(self,surface):

        x,y = self.pos
        
        body = pygame.draw.circle(WIN, (57, 45, 43), self.pos, 32)
        left_ear = pygame.draw.circle(WIN, (57, 45, 43), (x-25,y-20), 10)  
        right_ear = pygame.draw.circle(WIN, (57, 45, 43), (x+25, y-20), 10)  
        left_pink = pygame.draw.circle(WIN, (235, 150, 165), (x-25,y-20), 5)  
        right_pink = pygame.draw.circle(WIN, (235, 150, 165), (x+25, y-20), 5)  
        left_eye = pygame.draw.circle(WIN, (0, 0, 0), (x-12, y-5), 3)  
        right_eye = pygame.draw.circle(WIN, (0, 0, 0), (x+12, y-5), 3)  
        nose = pygame.draw.circle(WIN, (235, 150, 165), (x, y+15), 6)


    def change_pos(self):

        self.pos = rand_pos
        self.mole_rect.x, self.mole_rect.y = rand_pos


my_mole = Mole(rand_pos)



running = True

while running:

    frames.tick(FPS)

    WIN.fill(grass)
    
    pygame.draw.rect(WIN, (12,82,201),my_mole.mole_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:        
            print(f"The position is: {event.pos}!")
            my_mole.change_pos()

            flag_ = my_mole.mole_rect.collidepoint(event.pos)

            if flag_ == True:

                rand_pos  = random.choice(positions)
                rand_rect_pos = random.choice(mole_rect_pos)
                my_mole.mole_rect.x, my_mole.mole_rect.y = rand_rect_pos

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
