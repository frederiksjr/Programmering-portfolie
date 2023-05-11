import math
import tkinter as tk


def rotate(angle=0):
    x = math.cos(angle) * 200 + 250
    y = math.sin(angle) * 200 + 250
    canvas.coords(txt, x, y)
    canvas.after(100, rotate, angle+0.1)

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)

txt = canvas.create_text(250, 50, text='around and around')
rotate()
canvas.pack()
root.mainloop()