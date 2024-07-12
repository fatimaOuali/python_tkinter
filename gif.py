import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas

root = tk.Tk()
root.title("Alternate Circles GIF")
canvas = ScrolledCanvas(root)
canvas.pack(fill=tk.BOTH, expand=tk.YES)
t = RawTurtle(canvas)
t.speed(0)

def draw(size, num):
    for _ in range(num):
        if _ % 2 == 0:
            t.fillcolor("white")
        else:
            t.fillcolor("black")

        t.begin_fill()
        t.circle(size)
        t.end_fill()
        t.left(10)

frames = []
for i in range(36):
    t.clear()
    draw(50,100)
    frames.append(
        t.getscreen().getcanvas().postscript(
            colormode="color"
        )
    )

file_path = "alternate.gif"
canvas.postscript(
    file = file_path,
    colormode="color",
    width = canvas.winfo_width(),
    height = canvas.winfo_height()
)
root.destroy()

print(f"GIF saved to {file_path}")
