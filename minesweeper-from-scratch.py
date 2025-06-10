import os
import numpy as np
import tkinter as tk

rng = np.random.default_rng()
np.set_printoptions(linewidth=np.inf)
count = 0
level = 1
x = y = 9
m = 10
PADDING = "+1100+400"
current_bg = "beginner_template.png"


# Here are the map generation functions.


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


# Requires manual geometry management (pack, place, etc.).
def img(image):
    # Load an image and return it as a PhotoImage object.
    if os.name == "nt":
        return tk.PhotoImage(file=f".\\Images\\{image}")
    else:
        return tk.PhotoImage(file=f"./Images/{image}")


# Creates a canvas to display the background image.
class Canvas:

    def __init__(self):
        global current_bg
        screenw = root.winfo_screenwidth()
        screenh = root.winfo_screenheight()
        self.canvas = bg = tk.Canvas(
            root,
            width=screenw,
            height=screenh,
            highlightthickness=0
        )
        bg.place(x=0, y=0)
        self.img_bg = img(current_bg)
        bg.create_image(0, 0, anchor=tk.NW, image=self.img_bg)

    def add(self, coords, image):
        self.new_image = img(image)
        self.canvas.create_image(
            coords,
            anchor=tk.NW,
            image=self.new_image
        )

    def rid(self, image):
        self.canvas.delete(img(image))

    def replace(self, image1, image2, x, y):
        Canvas.rid(self, image1)
        Canvas.add(self, (x, y), image2)

    def resize(self, new_w, new_h):
        self.canvas.config(width=new_w, height=new_h)


# Creates a grid of buttons to interact with the game.
class Grid():

    def __init__(self):
        self.x = self.xcoord = 12
        self.y = self.ycoord = 55
        self.main_image = img("top_cell.png")

    def button(self, x, y):
        button = tk.Button(
            root,
            image=self.main_image,
            borderwidth=0,
            highlightthickness=0,
        )
        button.place(x=x, y=y)
        return button

    def kill(self):
        # Clear all buttons from the grid.
        for widget in root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

    def fill(self):
        Grid.kill(self)

        # Create new buttons
        for i in range(0, y):
            for j in range(0, x):
                self.x = self.xcoord + (i * 16)
                self.y = self.ycoord + (j * 16)

                Grid.button(self, self.x, self.y)


class Lvl:

    def change(lvl, geometry, bg_image):
        global level, current_bg
        level = lvl
        game(level)
        root.geometry(geometry)
        bg.replace(current_bg, bg_image, 0, 0)
        current_bg = bg_image
        grid.fill()

    def one():
        Lvl.change(
            1,
            "164x207",
            "beginner_template.png"
        )

    def two():
        Lvl.change(
            2,
            "276x319",
            "intermediate_template.png"
        )

    def three():
        Lvl.change(
            3,
            "500x319",
            "expert_template.png"
        )


def settings_menu():
    global level
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    settings_menu = tk.Menu(menubar, tearoff=False)
    settings_menu.add_command(
        label="New"
    )
    settings_menu.add_separator()
    settings_menu.add_command(
        label="Beginner",
        command=Lvl.one
    )
    settings_menu.add_command(
        label="Intermediate",
        command=Lvl.two
    )
    settings_menu.add_command(
        label="Expert",
        command=Lvl.three
    )
    settings_menu.add_separator()
    settings_menu.add_command(
        label="Marks (?)"
    )
    settings_menu.add_command(
        label="Chording"
    )
    settings_menu.add_separator()
    settings_menu.add_command(
        label="Best Times"
    )
    settings_menu.add_separator()
    settings_menu.add_command(
        label="Exit",
        command=root.destroy
    )

    menubar.add_cascade(
        label="Settings",
        menu=settings_menu
    )


def set_icon():
    if os.name == "nt":
        root.iconbitmap(".\\Images\\logo.ico")
    else:
        root.icon_photo = tk.PhotoImage(file="./Images/logo.png")
        root.iconphoto(False, root.icon_photo)


def main():
    global root, bg, grid, PADDING
    root = tk.Tk()
    root.title("Minesweeper - From Scratch")
    root.geometry(f"164x227{PADDING}")
    root.resizable(False, False)
    root.attributes("-topmost", 1)

    set_icon()

    bg = Canvas()
    grid = Grid()
    grid.fill()
    settings_menu()

    root.mainloop()


if __name__ == "__main__":
    main()