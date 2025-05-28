import pygame as pg
import numpy as np

rng = np.random.default_rng()
np.set_printoptions(linewidth=np.inf)
count = 0


def mines(level):
    global x, y, m
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
    
    zero = np.zeros((x + 2, y + 2), dtype=int)
    for i in range(0, x + 2):
        for j in range(0, y + 2):
            zero[i, j] = 11
    grid = np.arange(2, (x * y + 2))
    
    while len(grid[grid==99]) != m:
        random = rng.integers(0, x * y)
        grid[random] = 99

    for i in range(0, x * y):
        if grid[i] == 99:
            continue
        if grid[i] != 0:
            grid[i] = 0

    grid = grid.reshape(x, y)
    zero[1:x+1, 1:y+1] = grid

    return zero


def number_if(argument):
    global count
    if argument == 99: count+= 1


def find_number(grid, i, j):
    number_if(grid[i - 1, j - 1])
    number_if(grid[i - 1, j])
    number_if(grid[i - 1, j + 1])
    number_if(grid[i, j - 1])
    number_if(grid[i, j + 1])
    number_if(grid[i + 1, j - 1])
    number_if(grid[i + 1, j])
    number_if(grid[i + 1, j + 1])


def set_number(grid, i, j):
    global count
    if count != 0:
        grid[i, j] = count
    count = 0


def numbers(grid):
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if grid[i, j] == 99:
                continue
            find_number(grid, i, j)
            set_number(grid, i, j)
    return grid


print("\nDifficulty Level: Beginner")
print(numbers(mines(1)))
print("\nDifficulty Level: Intermediate")
print(numbers(mines(2)))
print("\nDifficulty Level: Expert")
print(numbers(mines(3)))
input()

exit()





# Don't read past this point.
# It is a work in progress.





class Rect():

    def cent(rect, cent_x, cent_y):
        rect.centerx = cent_x
        rect.centery = cent_y

#     def create(w, h, cent_x, cent_y):
#         rect = pg.Rect(w, h, w, h)
#         Rect.cent(rect, cent_x, cent_y)
#         return rect

#     def draw(color, w, h, cent_x, cent_y, width=None):
#         rect = Rect.create(w, h, cent_x, cent_y)
#         if width != None: pg.draw.rect(bg, color, rect, width)
#         else: pg.draw.rect(bg, color, rect)


class Font():

    def font(string, size, color, cent_x=None, cent_y=None):
        font = pg.font.Font(None, size)
        text = font.render(string, True, color, BG_COLOR)
        textpos = pg.Rect(text.get_rect())
        if cent_x and cent_y != None: Rect.cent(textpos, cent_x, cent_y)
        bg.blit(text, textpos)


# Initialization
pg.init()
screen = pg.display.set_mode((500, 620))
pg.display.set_caption("Minesweeper - From Scratch")
pg.mouse.set_visible(True)

# Background creation
bg = pg.Surface(screen.get_size())
bg = bg.convert()
BG_COLOR = (40, 40, 50)
bg.fill(BG_COLOR)

# Object preparation
clock = pg.time.Clock()

# Main loop
running = True
while running:
    clock.tick(60)

    # Input handling
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False

    # Visualization
    screen.blit(bg, (0, 0))
    pg.display.flip()

pg.quit()