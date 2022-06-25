import sys
import pygame
import random

max_x = 1200
max_y = 800

max_snow = 100
snow_size = 64

#-------------------------------------------------------------------------------------
class Snow():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_number = random.randint(1,4)
        self.image_filename = "/home/aburtasov/python/py_git/learn-py/snowfall/" + "snow" + str(self.img_number) + ".png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (snow_size,snow_size))
    
    
    def move_snow(self):
        
        self.y = self.y + self.speed
        if self.y > max_y:
            self.y = (0 - snow_size)
            
        i = random.randint(1,3)
        
        if i == 1 :  # move to right
            self.x = self.x + 1
            if self.x > max_x:
                self.x = (0 - snow_size)
        elif i == 2 :  # move left
            self.x = self.x - 1
            if self.x < (0 - snow_size):
                self.x = max_x
    
    
    def draw_snow(self):
         screen.blit(self.image,(self.x, self.y))
         
         
#----------------------------------------------------------------------------------------------
         
def initialize_snow(max_snow, snowfall):
    for i in range(0,max_snow):
        xx = random.randint(0, max_x)
        yy = random.randint(0, max_y)
        snowfall.append(Snow(xx,yy))
        

def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()
            

#------------------MAIN-----------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((max_x,max_y),pygame.FULLSCREEN)
bg_color = (0,0,0)

snowfall = []


initialize_snow(max_snow,snowfall)

while True:
    
    screen.fill(bg_color)
    
    check_for_exit()
    
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    
    pygame.display.flip()