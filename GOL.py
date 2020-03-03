import pygame
import random
import math

clock = pygame.time.Clock()
scl = 20
width = 800
height = 800
cols = int(width / scl)
rows = int(height / scl)
crashed = False
Display = pygame.display.set_mode((width, height))
MODE = False


def make2DArray(cols, rows):
    arr = [None] * int(cols)
    for i in range(cols):
        arr[i] = [None] * int(rows)
    return arr


grid = make2DArray(cols, rows)

for x in range(cols):
    for y in range(rows):
        grid[x][y] = random.randint(0,1)


def draw():
    for i in range(cols):
        for j in range(rows):
            x = i * scl
            y = j * scl
            color = 0
            if grid[i][j] == 1:
                color = 255
            else:
                color = 0
            pygame.draw.rect(Display, (color, color, color), (x, y, scl - 1, scl - 1))


def update(g):
    nextgrid = make2DArray(cols, rows)
    for x in range(cols):
        for y in range(rows):
            n = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    n += g[(x + i + cols) % cols][(y + j + rows) % rows]

            n -= grid[x][y]
            if g[x][y] == 0 and n == 3:
                nextgrid[x][y] = 1
            elif g[x][y] == 1 and (n < 2 or n > 3):
                nextgrid[x][y] = 0
            else:
                nextgrid[x][y] = g[x][y]
    g = nextgrid
    return g


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            state = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            print(pos)
            x = int(pos[0] / scl)
            y = int(pos[1] / scl)
            if grid[x][y] == 1:
                grid[x][y] = 0
            else:
                grid[x][y] = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                MODE = not MODE
    for i in range(cols):
        x = i * scl - 1
        pygame.draw.line(Display, (255, 255, 255), (x, height), (x, 0), 1)
        for j in range(rows):
            y = j * scl - 1
            pygame.draw.line(Display, (255, 255, 255), (0, y), (width, y), 1)
    draw()
    if MODE:
        grid = update(grid)
    pygame.display.update()
    clock.tick(10)
pygame.quit()
quit()
