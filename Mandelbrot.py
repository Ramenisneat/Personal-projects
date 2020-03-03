import pygame
import math
import numpy as np
from numba import jit
import colorsys
import time

start_time = time.time()
clock = pygame.time.Clock()
pygame.init()
width = 1000
height = 1000
Display = pygame.display.set_mode((width, height))
crashed = False

xmin = -2
xmax = 2
ymin = -2
ymax = 2
max = 1000
'''''
-0.74877 <= x <= -0.74872
0.065053 <= y <= 0.065103
2048 iterations max
'''

@jit
def cal():
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return r1, r2


@jit
def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n  #+ 1 - math.log(math.log2(abs(z)))
        z = z * z + c
    return maxiter

def plot(r1, r2):
    for x in range(width):
        for y in range(height):
            a = r1[x]
            b = r2[y]
            n = mandelbrot(a + 1j * b, max)
            hue = np.interp(int(255 * n / max), (0, 255), (0, 1))
            saturation = 1
            value = 1 if n < max else 0
            r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

            Display.set_at((x, y), (
                np.interp(r, (0, 1), (0, 255)), np.interp(g, (0, 1), (0, 255)), np.interp(b, (0, 1), (0, 255))))
    print("done")

while not crashed :
    Display.fill((0, 0, 0))
    r1, r2 = cal()
    plot(r1, r2)
    pygame.display.update()



"""""
Display.fill((0, 0, 0))
r1, r2 = cal()
plot(r1, r2)
pygame.image.save(Display, "Pygame.png")
print("finished!")
print("time elapsed: {:.2f}s".format(time.time() - start_time))
"""
pygame.quit()
quit()
