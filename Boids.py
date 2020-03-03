import pygame
import math
import random

clock = pygame.time.Clock()
pygame.init()
width = 800
height = 800
Display = pygame.display.set_mode((width, height))

class Boid:
    def __init__(self):
        self.pos=pygame.math.Vector2(random.randint(0,width),random.randint(0,height))
        self.v = pygame.math.Vector2(random.randint(1,5),random.randint(1,5))
        self.a = pygame.math.Vector2()
    def update(self):
        self.pos.__add__(self.v)
        self.v.__add__(self.a)
    def show(self):
        pygame.draw.circle(Display,(255,255,255),self.pos,10)

crashed = False
boids = [Boid() for i in range(20)]
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    Display.fill((0,0,0))
    for b in boids:
        b.update()
        b.show()



    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
