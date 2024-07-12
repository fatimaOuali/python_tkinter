from tkinter import *
import itertools

s = Tk()
s.geometry('300x500')
s.configure(bg="black")

def button(x, y, text):
    c = itertools.cycle([
        'cyan','purple','pink','yellow'
    ])
    mb = Button(width=len(text)+2, height=2,
                text=text, fg='cyan',
                bg='black', border=0,
                activeforeground='black',
                activebackground='cyan',
                font=("Arial", 16, "bold"))
    def acolor():
        mb.config(bg=next(c))
        global animation
        animation = s.after(500, acolor)
    def enter(e):
        mb.config(bg=next(c),fg='black')
        acolor()
    def leave(e):
        mb.config(bg='black', fg='cyan')
        s.after_cancel(animation)

    mb.bind("<Enter>", enter)
    mb.bind("<Leave>", leave)
    mb.place(x=x, y=y)
animation = None
button(50, 50, "BUTTON")
s.mainloop()
