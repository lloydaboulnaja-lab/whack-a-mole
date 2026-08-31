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