import pygame
import math


clock = pygame.time.Clock()
pygame.init()
width = 800
height = 500
l = 150
a = 45
Display = pygame.display.set_mode((width,height))
tree = []
class Branch:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def show(self):
        pygame.draw.line(Display,(0,0,0),self.start,self.end)

    def right(self):
        d = (pygame.math.Vector2(self.end)-pygame.math.Vector2(self.start)).rotate(a)*.675
        newEnd = d + pygame.Vector2(self.end)
        tree.append(Branch(self.end,newEnd))
    def left(self):
        d = (pygame.math.Vector2(self.end)-pygame.math.Vector2(self.start)).rotate(-a)*.675
        newEnd = d + pygame.Vector2(self.end)
        tree.append(Branch(self.end,newEnd))

crashed = False
tree.append(Branch((width/2,height),(width/2,height-l)))
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    Display.fill((255,255,255))

    for b in tree:
        b.show()
        if len(tree) <5000:
            b.right()
            b.left()
    a=a+1
    tree.clear()
    tree.append(Branch((width/2,height),(width/2,height-l)))


    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
