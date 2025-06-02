import pygame as pg
import numpy as np


def mines(level):
    global x, y, m
    # Change the size and number of mines according to the difficulty level.
    if level == 1:
        x = y = 9
        m = 10
    if level == 2:
        x = y = 16
        m = 40
    if level == 3:
        x = 16
        y = 30
        m = 99

    # Create a new grid.
    grid = np.arange(2, (x * y + 2))

    # Until there are 99 mines, place a mine in a random spot.
    while len(grid[grid==99]) != m:
        random = rng.integers(0, x * y)
        grid[random] = 99

    # Change all non-mine spots to 0.
    for i in range(0, x * y):
        if grid[i] == 99: continue
        if grid[i] != 0: grid[i] = 0

    grid = grid.reshape(x, y)

    return grid


def border(grid):
    # Create a new grid with every spot as 11.
    border = np.array([11 for i in range(0, (x + 2) * (y + 2))])

    border = border.reshape(x + 2, y + 2)

    # Broadcast the grid with mines onto the border grid.
    border[1:x+1, 1:y+1] = grid

    return border


class Num:

    def check(argument):
        global count
        if argument == 99: count+= 1

    # Check all surrounding squares for a mine.
    def find(grid, i, j):
        Num.check(grid[i - 1, j - 1])
        Num.check(grid[i - 1, j])
        Num.check(grid[i - 1, j + 1])
        Num.check(grid[i, j - 1])
        Num.check(grid[i, j + 1])
        Num.check(grid[i + 1, j - 1])
        Num.check(grid[i + 1, j])
        Num.check(grid[i + 1, j + 1])

    def set(grid, i, j):
        global count
        grid[i, j] = count
        count = 0

    # Repeat the 'find' and 'set' functions for every square.
    def repeat(grid):
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if grid[i, j] == 99: continue
                Num.find(grid, i, j)
                Num.set(grid, i, j)
        return grid


def game(level):
    # Returns a ready-to-use grid w/o the border.
    return Num.repeat(
        border(mines(level))
    )[1:x+1, 1:y+1]


class Rect():

    def __init__(self, w, h, x, y):
        self.rect = pg.Rect(w, h, w, h)
        self.rect.x = x
        self.rect.y = y

    def draw(self, color, width=0):
        pg.draw.rect(bg, color, self.rect, width)


def font(string, size, color, bg_color, x=0, y=0):
    font = pg.font.Font(None, size)
    text = font.render(string, True, color, bg_color)
    textpos = pg.Rect(text.get_rect())
    textpos.x = x
    textpos.y = y
    bg.blit(text, textpos)


class Settings:

    def __init__(self):
        self = font("Settings", 18, "black", "white", 5, 5)

    def options():
        """
        New
        ---
        Beginner
        Intermediate
        Expert
        Custom - screen
        ---
        Marks (?)
        Chording - screen
        ---
        Best Times
        ---
        Exit
        """
        pass

    def bar():
        Rect.draw(Rect(250, 22, 0, 0), "white")


class Top:

    def mines_left():
        pass

    def new_game():
        pass

    def time():
        pass


# Initialization
pg.init()
screen = pg.display.set_mode((250, 320))
pg.display.set_caption("Minesweeper - From Scratch")
pg.mouse.set_visible(True)

# Background creation
bg = pg.Surface(screen.get_size())
bg = bg.convert()
BG_COLOR = (193, 192, 190)
bg.fill(BG_COLOR)

# Object preparation
clock = pg.time.Clock()
rng = np.random.default_rng()
np.set_printoptions(linewidth=np.inf)
count = 0

# Colors
EMPTY = "gray75"
BORDER = "gray50"
ONE = "blue2"
TWO = "green4"
THREE = "red"
FOUR = "navyblue"
FIVE = "darkred"
SIX = "darkcyan"
SEVEN = "black"
EIGHT = "gray50"

# Main loop
running = True
while running:
    clock.tick(60)

    # Input handling
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False

    Settings.bar()
    Settings()

    # Visualization
    screen.blit(bg, (0, 0))
    pg.display.flip()

pg.quit()