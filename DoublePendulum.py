import math

import pygame
import thorpy

pygame.init()
clock = pygame.time.Clock()
width = 700
height = 700
crashed = False
pygame.key.set_repeat(300, 30)
Display = pygame.display.set_mode((width, height))
slider1 = thorpy.SliderX(100, (5, 45), "m1", type_=int, initial_value=20)
slider2 = thorpy.SliderX(100, (5, 45), "m2", type_=int, initial_value=20)
slider3 = thorpy.SliderX(100, (50, 500), "r1", type_=int, initial_value=100)
slider4 = thorpy.SliderX(100, (50, 500), "r2", type_=int, initial_value=100)
slider5 = thorpy.SliderX(100, (0, 360), "a1", type_=int, initial_value=0)
slider6 = thorpy.SliderX(100, (0, 360), "a2", type_=int, initial_value=0)

r1 = slider3.get_value()
r2 = slider4.get_value()
m1 = slider1.get_value()
m2 = slider2.get_value()
a1 = math.pi / 2
a2 = math.pi / 2
g = 1
a1_v = 0
a2_v = 0
a1_a = 1
a2_a = 1
x2 = 0
y2 = 0
points = []
dragging = False

box = thorpy.Box(elements=[slider1, slider2, slider3, slider4])
menu = thorpy.Menu(box)
for element in menu.get_population():
    element.surface = Display

box.set_topleft((500, 200))

while not crashed:

    x1 = round(250 + (r1 * math.sin(a1)))
    y1 = round(100 + (r1 * math.cos(a1)))
    x2 = round(x1 + (r2 * math.sin(a2)))
    y2 = round(y1 + (r2 * math.cos(a2)))

    for event in pygame.event.get():
        menu.react(event)
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                points.clear()
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mx, my = event.pos
                a2 = -math.atan2(my -y1, mx - x1)

    if not dragging:
        try:
            den = 2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2)
            a1_a = (-g * (2 * m1 + m2) * math.sin(a1) - m2 * g * math.sin(a1 - 2 * a2) - 2 * math.sin(a1 - a2) * m2 * (
                    a2_v ** 2 * r2 + a1_v ** 2 * r1 * math.cos(a1 - a2))) / (r1 * den)
            a2_a = (2 * math.sin(a1 - a2) * (
                    a1_v ** 2 * r1 * (m1 + m2) + g * (m1 + m2) * math.cos(a1) + a2_v ** 2 * r2 * m2 * math.cos(
                a1 - a2))) / (r2 * den)
            a1_v += a1_a
            a2_v += a2_a
            a1 += a1_v
            a2 += a2_v
            points.append((x2, y2))
        except:
            a1_v = a1_v
            a2_v = a2_v

    Display.fill((255, 255, 255))
    box.blit()
    r1 = slider3.get_value()
    r2 = slider4.get_value()
    m1 = slider1.get_value()
    m2 = slider2.get_value()

    pygame.draw.line(Display, (0, 0, 0), (250, 50), (x1, y1), 3)
    pygame.draw.line(Display, (0, 0, 0), (x1, y1), (x2, y2), 3)
    pygame.draw.circle(Display, (0, 0, 255), (x1, y1), m1)
    pygame.draw.circle(Display, (0, 0, 255), (int(x2), int(y2)), m2)

    if len(points) != 1:
        pygame.draw.lines(Display, (0, 0, 0), False, points, 2)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
