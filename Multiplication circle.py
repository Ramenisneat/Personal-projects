import math

import pygame
import thorpy

clock = pygame.time.Clock()
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 15)
width = 800
height = 500
Display = pygame.display.set_mode((width, height))
animate = False



crashed = False
points = []
inserter = thorpy.Inserter(name="Factor: ", value="2")
slider2 = thorpy.SliderX(150, (1, 200), "# of points", type_=int, initial_value=200)
factor = int(inserter.get_value())
n = slider2.get_value()
radius = 250

box = thorpy.Box(elements=[inserter, slider2])
menu = thorpy.Menu(box)
for element in menu.get_population():
    element.surface = Display

box.set_topleft((500, 300))
textsurface = myfont.render('Toggle animation by pressing the spacebar', False, (0, 0, 0))

def calPoints(n):
    points.clear()
    t = (math.pi * 2) / n
    angle = 0
    for i in range(n):
        x = radius + radius * math.sin(angle)
        y = radius + radius * math.cos(angle)
        points.append((round(x), round(y)))
        angle += t


while not crashed:

    for event in pygame.event.get():
        menu.react(event)

        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                animate = not animate

    if animate == False:
        if inserter.get_value() == "":
            factor = 0
        else:
            factor = int(inserter.get_value())
    else:
        factor += .01
        inserter.set_value(str(math.floor(factor)))

    n = slider2.get_value()
    calPoints(n)
    Display.fill((255, 255, 255))
    pygame.draw.circle(Display, (0, 0, 0), (radius, radius), radius, 2)
    for p in points:
        pygame.draw.circle(Display, (0, 0, 0),p, 3, 2)

    for i in range(len(points)):
        index = math.floor((i * factor) % n)
        pygame.draw.line(Display, (0, 0, 0), points[i], points[index])
    box.blit()
    Display.blit(textsurface,(520,200))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
