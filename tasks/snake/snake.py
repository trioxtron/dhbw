import random
import pygame

class Cube(object):
    rows = 20
    w = 500
    def __init__(self, start, color=(0, 0, 255)):
        self.pos = start
        self.color = color

        self.x = [0, -1, 0, 1]
        self.y = [1, 0, -1, 0]
        self.dir = 3


    def move(self):
        x = self.pos[0] + self.x[self.dir]
        y = self.pos[1] + self.y[self.dir]
        self.pos = (x, y)


    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class Snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.x = [0, -1, 0, 1]
        self.y = [1, 0, -1, 0]
        self.dir = 0 

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_h]:
                if self.dir != 1 and self.dir != 3:
                    self.dir = 1
                    self.turns[self.head.pos[:]] = self.dir

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_l]:
                if self.dir != 3 and self.dir != 1:
                    self.dir = 3
                    self.turns[self.head.pos[:]] = self.dir

            elif keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_k]:
                if self.dir != 2 and self.dir != 0:
                    self.dir = 2
                    self.turns[self.head.pos[:]] = self.dir

            elif keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_j]:
                if self.dir != 0 and self.dir != 2:
                    self.dir = 0
                    self.turns[self.head.pos[:]] = self.dir

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn_dir = self.turns[p]
                c.dir = turn_dir
                c.move()
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dir == 1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dir == 3 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dir == 0 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dir == 2 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move()


    def addCube(self):
        tail = self.body[-1]

        if tail.dir == 3:
            self.body.append(Cube((tail.pos[0]-1,tail.pos[1])))
        elif tail.dir == 1:
            self.body.append(Cube((tail.pos[0]+1,tail.pos[1])))
        elif tail.dir == 0:
            self.body.append(Cube((tail.pos[0],tail.pos[1]-1)))
        elif tail.dir == 2:
            self.body.append(Cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dir = tail.dir
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir = 3


def redrawWindow(surface):
    global rows, width, s, food
    surface.fill((0, 0, 0))
    s.draw(surface)
    food.draw(surface)
    
    pygame.display.update()


def randomFood(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)


def main():
    global width, rows, s, food
    width = 500
    rows = 20
    highscore = 0
    win = pygame.display.set_mode((width, width))
    s = Snake((0, 0, 255), (10, 10))
    food = Cube(randomFood(rows, s), color=(0, 255, 0))

    windowicon = pygame.image.load("./snake_icon.jpg")
    pygame.display.set_icon(windowicon)

    pygame.display.set_caption("Snake made by noah")
    
    while True:
        pygame.time.delay(60)
        s.move()
        bodycount = len(s.body)
        if s.body[0].pos == food.pos:
            s.addCube()
            food = Cube(randomFood(rows, s), color=(0, 255, 0))

            pygame.display.set_caption(f"snake made by noah; session highscore: {highscore}; current score: {bodycount}")

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print(f'score: {bodycount - 1}')

                if bodycount > highscore:
                    highscore = bodycount - 1 

                s.reset((10, 10))
                break

        redrawWindow(win)

main()
