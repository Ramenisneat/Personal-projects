import pygame
import math


clock = pygame.time.Clock()
pygame.init()
width = 500
height = 500
n =0
c = 10
Display = pygame.display.set_mode((width,height))



        
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    a = n*137.5
    r = c* math.sqrt(n)
    x =round( width/2+r*math.cos(a))
    y = round(height/2+r*math.sin(a))

    pygame.draw.circle(Display,(0,0,255),(x,y), 5)
    
    n+=1
    pygame.display.update()
    clock.tick(24)
pygame.quit()
quit()
