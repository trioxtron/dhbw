import random
import pygame
from snake import Snake, Cube

def redrawWindow(surface, s1, s2, food):
    """Redraw the window with the snakes and food
    Args:
        surface (Surface): The window to draw on
        s1 (Snake): The first snake
        s2 (Snake): The second snake
        food (Cube): The food
    """
    surface.fill((0, 0, 0))
    s1.draw(surface)
    s2.draw(surface)
    food.draw(surface)
    
    pygame.display.update()


def random_food(rows, snake1, snake2):
    """Generate random food for the snakes
    Args:
        rows (int): The number of rows in the game
        snake1 (Snake): The first snake
        snake2 (Snake): The second snake
    Returns:
        Tuple: The position of the food
    """
    positions1 = snake1.body
    positions2 = snake2.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(int(rows*0.8))
        if len(list(filter(lambda z:z.pos == (x,y), positions1))) > 0 or len(list(filter(lambda z:z.pos == (x,y), positions2))) > 0:
            continue
        else:
            break
        
    return (x,y)


def next_move(s, opp, keys):
    """Move the snake and check for collisions
    Args:
        s (Snake): The snake that is moving
        opp (Snake): The other snake
        keys (Dict): The keys that are pressed
    """
    s.move(keys)

    if s.head.pos in list(map(lambda z:z.pos,opp.body[1:])):
        if len(s.body) > 1:
            opp.addCube(len(s.body)-1)
            s.reset((10, 10))

    for x in range(len(s.body)):
        if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
            s.reset((10, 10))
            break


def get_inputs():
    """Get the inputs from the players
    Returns:
        Dict: The keys that are pressed
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()
        if keys != None:
            return keys


def get_color():
    """Get the color of the snake from the user
    Returns:
        Tuple: The RGB value of the snake
    """
    print("\nWhat color do you want?\n 1. Red\n 2. Blue\n 3. Pink\n 4. Yellow\n Specific color")
    color = input("Enter the number of your choice: ")
    if color == "1":
        return (255, 0, 0)
    elif color == "2":
        return (0, 0, 255)
    elif color == "3":
        return (255, 0, 255)
    elif color == "4":
        return (255, 255, 0)
    elif color == "5":
        r = int(input("Enter the red value: "))
        g = int(input("Enter the green value: "))
        b = int(input("Enter the blue value: "))
        return (r, g, b)
    else:
        return get_color()


def start_game(rows, width):
    """Start the game and return the two snakes and the food
    Args:
        rows (int): The number of rows in the game
        width (int): The width of the window
    Returns:
        Snake: The first snake
        Snake: The second snake
        Cube: The food
    """
    print("Welcome to Snake!")
    print("The first player is going to use WASD and the second player is going to use the arrow keys.\n")

    color = get_color()
    s1 = Snake(color, (10, 10), rows, width, "wasd")

    color = get_color()
    s2 = Snake(color, (10, 10), rows, width, "arrows")
    food = Cube(random_food(rows, s1, s2), rows, width, color=(0, 255, 0))

    windowicon = pygame.image.load("./snake_icon.jpg")
    pygame.display.set_icon(windowicon)
    pygame.display.set_caption("Snake made by noah")

    print("\n\nGood luck!\n")
    print("Press any key to start the game.")
    input()
    return s1, s2, food


def main():
    """Main function to run the game"""
    width = 1000
    rows = 40
    win = pygame.display.set_mode((width, width*0.8))

    s1, s2, food = start_game(rows, width)
    
    while True:
        # Delay to make the game run at a reasonable speed
        pygame.time.delay(60)

        # Get all current inputs from both players 
        keys = get_inputs()

        # Move snakes and check for collisions 
        next_move(s1, s2, keys)
        next_move(s2, s1, keys)

        # Check if snake eats food
        if s1.body[0].pos == food.pos:
            s1.addCube()
            food = Cube(random_food(rows, s1, s2), rows, width, color=(0, 255, 0))
        if s2.body[0].pos == food.pos:
            s2.addCube()
            food = Cube(random_food(rows, s1, s2), rows, width, color=(0, 255, 0))

        pygame.display.set_caption(f"snake made by noah - WASD: {len(s1.body)} - ARROWS: {len(s2.body)}")
        redrawWindow(win, s1, s2, food)


if __name__ == "__main__":
    main()
