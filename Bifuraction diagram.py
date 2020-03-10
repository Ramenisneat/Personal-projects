import random
import numpy as np
import pygame

clock = pygame.time.Clock()
width = 400
height = 400
pygame.init()
Display = pygame.display.set_mode((width, height))
r = 2.6
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    #Display.fill((0, 0, 0))
    pop = 1
    for i in range(30):
        pop =  pop*r*(1-r)
    
        yval = np.interp(pop,(0,1),(0,height))
        xval = np.interp(i,(0,30),(0,width))
        pygame.draw.circle(Display,(0,0,255),(xval,yval),10)


    pygame.display.update()
    clock.tick(5)
pygame.quit()
quit()
