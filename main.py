import pygame, sys    # importing necessary libs
from pygame.locals import *  
import random


pygame.init()   

WIDTH, HEIGHT = 900, 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Whack A Mole!") 

grass = (34, 139, 34)

text_font = pygame.font.SysFont("Arial", 40, bold=True)

FPS = 60

score = 0 

game_state = "playing"

frames = pygame.time.Clock()

positions = [
(190, 230),
(440, 230),
(690, 230),(190, 480),
(440, 480),(690, 480)]

rand_pos  = random.choice(positions)


def draw(text, font, color, x, y,):  # drawing the score text at the top left of the window
    img = font.render(text,True, color)
    WIN.blit(img, (x, y))


class Mole:

    ''' Created a mole object to own its attributes like its position
    and to perform functions like moving itself
    '''

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
         
        rand_pos = random.choice(positions)

        self.pos = rand_pos

        x, y = rand_pos

        self.mole_rect.x = x - 25
        self.mole_rect.y = y - 35

        

my_mole = Mole(rand_pos)

running = True

last_moved = pygame.time.get_ticks()

current_time = pygame.time.get_ticks()

def playing_game():

    frames.tick(FPS)
    
    
    
    if current_time - last_moved >= 1000:
        my_mole.change_pos()


        last_moved = current_time
            
    
    WIN.fill(grass)
        
    pygame.draw.rect(WIN, (34, 139, 34, 0.5),my_mole.mole_rect)
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        elif event.type == MOUSEBUTTONDOWN:    
                   
            if my_mole.mole_rect.collidepoint(event.pos) == True:  # detecting if the mole has been hit
    
                score += 1
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
    
        draw(f"SCORE: {score}",text_font, (12,98,205), 20, 20)



while running:  # main game loop

    if game_state == "playing":

        playing_game()

    else:

        pass
   
    pygame.display.flip()