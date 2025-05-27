import pygame as pg
import numpy as np

rng = np.random.default_rng()

x = np.arange(2, 83)

def place_mines(x):
    while len(x[x==1]) != 10:
        random = rng.integers(2, 83)
        x[random] = 1

place_mines(x)

x = x.reshape(9, 9)

print(x)

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