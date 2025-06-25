import pygame

class Cube(object):
    def __init__(self, start, rows, w, color):
        """Initialize the cube
        Args:
            start (Tuple): The starting position of the cube
            rows (int): The number of rows in the game
            w (int): The width of the window
            color (Tuple): The RGB value of the cube
        """
        self.pos = start
        self.color = color
        self.rows = rows
        self.w = w

        self.x = [0, -1, 0, 1]
        self.y = [1, 0, -1, 0]
        self.dir = 3


    def move(self):
        """Move the cube in the direction of the snake"""
        x = self.pos[0] + self.x[self.dir]
        y = self.pos[1] + self.y[self.dir]
        self.pos = (x, y)


    def draw(self, surface, eyes=False):
        """Draw the cube on the window
        Args:
            surface (Surface): The window to draw on
            eyes (bool): Whether to draw the eyes of
        """
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
    """Class to represent the snake in the game"""
    body = []
    turns = {}
    def __init__(self, color, pos, rows, w, key_type):
        """Initialize the snake
        Args:
            color (Tuple): The RGB value of the snake
            pos (Tuple): The starting position of the snake
            rows (int): The number of rows in the game
            w (int): The width of the window
            key_type (str): The type of keys used by the player
        """
        self.color = color
        self.rows = rows
        self.w = w
        self.head = Cube(pos, rows, w, self.color)
        self.body.append(self.head)
        self.x = [0, -1, 0, 1]
        self.y = [1, 0, -1, 0]
        self.dir = 0 
        self.key_type = key_type

    def move(self, keys):
        """Move the snake in the direction of the keys pressed
        Args:
            keys (Dict): The keys that are pressed
        """
        if keys != None:
            if self.key_type == "wasd":
                if keys[pygame.K_a]:
                    if self.dir != 1 and self.dir != 3:
                        self.dir = 1
                        self.turns[self.head.pos[:]] = self.dir

                elif keys[pygame.K_d]:
                    if self.dir != 3 and self.dir != 1:
                        self.dir = 3
                        self.turns[self.head.pos[:]] = self.dir

                elif keys[pygame.K_w]:
                    if self.dir != 2 and self.dir != 0:
                        self.dir = 2
                        self.turns[self.head.pos[:]] = self.dir

                elif keys[pygame.K_s]:
                    if self.dir != 0 and self.dir != 2:
                        self.dir = 0
                        self.turns[self.head.pos[:]] = self.dir

            elif self.key_type == "arrows":
                if keys[pygame.K_LEFT]:
                    if self.dir != 1 and self.dir != 3:
                        self.dir = 1
                        self.turns[self.head.pos[:]] = self.dir

                elif keys[pygame.K_RIGHT]:
                    if self.dir != 3 and self.dir != 1:
                        self.dir = 3
                        self.turns[self.head.pos[:]] = self.dir

                elif keys[pygame.K_UP]:
                    if self.dir != 2 and self.dir != 0:
                        self.dir = 2
                        self.turns[self.head.pos[:]] = self.dir

                elif keys[pygame.K_DOWN]:
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
                elif c.dir == 0 and c.pos[1] >= (c.rows*0.8)-1: c.pos = (c.pos[0], 0)
                elif c.dir == 2 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move()


    def addCube(self, n=1):
        """Add a cube to the snake
        Args:
            n (int): The number of cubes to add
        """
        for _ in range(n):
            tail = self.body[-1]

            if tail.dir == 3:
                self.body.append(Cube((tail.pos[0]-1,tail.pos[1]), self.rows, self.w, self.color))
            elif tail.dir == 1:
                self.body.append(Cube((tail.pos[0]+1,tail.pos[1]), self.rows, self.w, self.color))
            elif tail.dir == 0:
                self.body.append(Cube((tail.pos[0],tail.pos[1]-1), self.rows, self.w, self.color))
            elif tail.dir == 2:
                self.body.append(Cube((tail.pos[0],tail.pos[1]+1), self.rows, self.w, self.color))

            self.body[-1].dir = tail.dir
        

    def draw(self, surface):
        """Draw the snake on the window
        Args:
            surface (Surface): The window to draw on
        """
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


    def reset(self, pos):
        """Reset the snake to the starting position
        Args:
            pos (Tuple): The starting position of the snake
        """
        self.head = Cube(pos, self.rows, self.w, self.color)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir = 3
