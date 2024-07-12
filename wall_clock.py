import tkinter as tk
import time
import math

root = tk.Tk()
cn = tk.Canvas(root, width=400, height=400,
               bg='white')
cn.pack()
cx, cy = 200, 200
r = 180

cn.create_oval(cx-r, cy-r, cx+r, cy+r)
for i in range(1, 13):
    ang = math.pi / 6 * (i - 3)
    x = cx + r * 0.85 * math.cos(ang)
    y = cy + r * 0.85 * math.sin(ang)
    cn.create_text(x, y, text=str(i),
                   font=("Arial",16,"bold"))

def update_time():
    c = time.localtime()
    s = math.pi/30 * c.tm_sec-math.pi/2
    m = math.pi/30 * c.tm_min-math.pi/2
    h = math.pi/6 * (
        c.tm_hour%12 + c.tm_min/60
    )- math.pi/2
    cn.delete("hands")
    for ang, lg, width, color in [
        (s, 0.9, 1, "red"),
        (m, 0.7, 2, "black"),
        (h, 0.5, 4, "black"),
    ]:
        x = cx + r * lg * math.cos(ang)
        y = cy + r * lg * math.sin(ang)
        cn.create_line(cx, cy, x, y,
                       width=width,
                       fill=color,
                       tags="hands")
    root.after(1000, update_time)
update_time()
root.mainloop()