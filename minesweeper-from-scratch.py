import os
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

rng = np.random.default_rng()
np.set_printoptions(linewidth=np.inf)
count = 0
level = 1
x = y = 9
m = 10
padding = "+300+400"


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
class Img:

    def sing(name):
        image = Image.open(".\\Images\\" + str(name))
        py_image = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=py_image)
        return label

    def mult(name):
        image = Image.open(".\\Images\\" + str(name))
        py_image = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=py_image)
        label.photo = py_image
        return label


class Lvl:

    def set(lvl):
        global level
        if level != lvl: level = lvl

    def one():
        Lvl.set(1)
        root.geometry("166x207")
        Img.sing("beginner_template.jpg").place(x=0, y=0)

    def two():
        Lvl.set(2)
        root.geometry("278x321")
        Img.sing("intermediate_template.jpg").place(x=0, y=0)

    def three():
        Lvl.set(3)
        root.geometry("502x321")
        Img.sing("expert_template.jpg").place(x=0, y=0)


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


root = tk.Tk()
root.title("Minesweeper - From Scratch")
root.geometry(f"166x228{padding}")
root.resizable(False, False)
root.attributes("-topmost", 1)

if os.name == "nt": root.iconbitmap(".\\Images\\logo.ico")
else: root.iconphoto(False, tk.PhotoImage(file=".\\Images\\logo.png"))

Img.sing("beginner_template.jpg").place(x=0, y=0)

settings_menu()

root.mainloop()