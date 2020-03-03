import random

import pygame

clock = pygame.time.Clock()
scl = 20
width = 400
height = 400
cols = width / scl
rows = height / scl
snake = []
pygame.init()
Display = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('helvetica.ttf', 20)


class Snake:
    def __init__(self, x, y, xsp, ysp):
        self.x = x
        self.y = y
        self.xsp = xsp
        self.ysp = ysp
        self.score = 0
        self.color = (random.randint(0, 255), 255, 0)

    def update(self):
        if self == s:
            self.x += self.xsp * scl
            self.y += self.ysp * scl
        else:
            self.x = snake[snake.index(self) - 1].x - (snake[snake.index(self) - 1].xsp * scl)
            self.y = snake[snake.index(self) - 1].y - (snake[snake.index(self) - 1].ysp * scl)
        if self.x > width or self.x < 0 or self.y > height or self.y < 0:
            pygame.quit()
            quit()
        for i in range(1, len(snake)):
            if s.x == snake[i].x and s.y == snake[i].y:
                pygame.quit()
                quit()

    def show(self):
        Display.fill(self.color, rect=[self.x, self.y, scl, scl])


class food:
    def __init__(self):
        self.x = random.randrange(cols) * scl
        self.y = random.randrange(rows) * scl

    def show(self):
        Display.fill((255, 0, 0), rect=[self.x, self.y, scl, scl])

    def update(self, s):
        if s.x == self.x and s.y == self.y:
            self.__init__()
            s.score += 1
            print(s.score)
            l = len(snake) - 1
            snake.append(Snake(snake[l].x + snake[l].xsp, snake[l].y + snake[l].ysp, 0, 0))


s = Snake(0, 0, 0, 0)
snake.append(s)
s.color = (0, 255, 255)
f = food()
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                s.xsp = -1
                s.ysp = 0
            if event.key == pygame.K_RIGHT:
                s.xsp = 1
                s.ysp = 0
            if event.key == pygame.K_UP:
                s.xsp = 0
                s.ysp = -1
            if event.key == pygame.K_DOWN:
                s.xsp = 0
                s.ysp = 1

    Display.fill((0, 0, 0))
    textsurface = font.render('Score:' + str(s.score), False, (255, 255, 255))
    f.update(s)
    f.show()
    s.update()
    for i in range(len(snake) - 1, 0, -1):
        snake[i].update()
        snake[i].show()

    s.show()
    Display.blit(textsurface, (0, 0))
    pygame.display.update()
    clock.tick(8)
pygame.quit()
quit()
