import pygame
import math
import random

clock = pygame.time.Clock()
pygame.init()
width = 1280
height = 720
Display = pygame.display.set_mode((width, height))

def limit(v,max):
    if v.magnitude()>max:
        v.normalize()
        v *= max

def set_mag (v,mag):
    v.normalize()
    v*=mag

class Boid:
    def __init__(self):
        self.pos=pygame.math.Vector2(random.randint(0,width),random.randint(0,height))
        self.v = pygame.math.Vector2(random.randrange(-3,3) ,random.randrange(-3,3))
        try:
            self.v.normalize()
        except ValueError:
            pass
        self.v *= random.randrange(2,4)
        self.a = pygame.math.Vector2()
        self.maxForce = .2
        self.maxSpeed = 2

    def update(self):
        self.pos+=self.v
        self.pos.x %= width
        self.pos.y %= height
        self.v+=self.a

    def show(self):
        pygame.draw.circle(Display,(255,255,255),self.pos,10)

    def flock(self,boids):
        self.a *=0
        self.a += self.Seperation(boids)
        self.a += self.align(boids)
        self.a += self.cohesion(boids)



    def align(self,boids):
        max_dis = 50
        avg = pygame.math.Vector2()
        local_pop = 0
        for boid in boids:
            d = math.dist((self.pos.x,self.pos.y),(boid.pos.x,boid.pos.y))
            if d<max_dis and boid!=self:
                avg+=boid.v
                local_pop+=1

        if local_pop>0 and avg.magnitude()!= 0:
            avg/= local_pop
            #set_mag(avg,self.maxSpeed)
            avg-=self.v
            limit(avg,self.maxForce)

        return avg

    def cohesion(self, boids):
        max_dis = 50
        avg_point = pygame.math.Vector2()
        local_pop = 0
        for boid in boids:
            d = math.dist((self.pos.x, self.pos.y), (boid.pos.x, boid.pos.y))
            if d < max_dis and boid != self:
                avg_point += boid.pos
                local_pop += 1
        if local_pop > 0:
            avg_point /= local_pop
            avg_point -=self.pos
            avg_point -= self.v
            limit(avg_point, self.maxForce)

        return avg_point

    def Seperation(self, boids):
        max_dis = 50
        avg_point = pygame.math.Vector2()
        local_pop = 0
        for boid in boids:
            d = math.dist((self.pos.x, self.pos.y), (boid.pos.x, boid.pos.y))
            if d < max_dis and boid != self:
                dif = self.pos - boid.pos
                dif /= d
                avg_point += dif
                local_pop += 1
        if local_pop > 0:
            avg_point /= local_pop
            avg_point -= self.v


        return avg_point


crashed = False
flock = [Boid() for i in range(50)]
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    Display.fill((0,0,0))
    for b in flock:
        b.flock(flock)
        b.update()
        b.show()


    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
