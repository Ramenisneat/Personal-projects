import time

import numpy as np
from PIL import Image, ImageDraw
from numba import jit

start_time = time.time()
height = 1000
width = 1000
xmin = -0.74877
xmax = -0.74872
ymin = 0.065053
ymax = 0.065103
max = 2048
'''''
-0.74877 <= x <= -0.74872
0.065053 <= y <= 0.065103
2048 iterations max
'''

r1 = np.linspace(xmin, xmax, width)
r2 = np.linspace(ymin, ymax, height)
img = Image.new('HSV', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(img)


@jit
def mandelbrot(r, i, x):
    a = r
    b = i
    for n in range(x):
        a2 = a * a
        b2 = b * b
        if a2 + b2 > 4.0:
            return n
        b = 2 * a * b + i
        a = a2 - b2 + r
    return x


def plot():
    for x in range(width):
        for y in range(height):
            n = mandelbrot(r1[x], r2[y], max)
            h = int(255 * n / max)
            s = 255
            v = 255 if n < max else 0
            draw.point([x, y], (h, s, v))


plot()
img.convert("RGB").save("Image.png", "PNG")
print("finished!")
print("time elapsed: {:.2f}s".format(time.time() - start_time))
