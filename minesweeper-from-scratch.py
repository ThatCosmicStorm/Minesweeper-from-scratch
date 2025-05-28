import pygame as pg
import numpy as np

rng = np.random.default_rng()

def mines(level):
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
    grid = np.arange(2, (x * y + 2))
    
    while len(grid[grid==1]) != m:
        random = rng.integers(0, x * y)
        grid[random] = 1

    for i in range(0, x * y):
        if grid[i] == 1:
            continue
        if grid[i] != 2:
            grid[i] = 2

    grid = grid.reshape(x, y)
    zero[1:x+1, 1:y+1] = grid

    return zero

print("\nDifficulty Level: Beginner")
print(mines(1))
print("\nDifficulty Level: Intermediate")
print(mines(2))
print("\nDifficulty Level: Expert")
print(mines(3))

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