import tkinter as tk

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
    
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("240x300")
    root.configure(bg="gray")

    expression = ""
    equation = tk.StringVar()

    entry = tk.Entry(
        root, textvariable=equation,
        font=('Helvetica', 14),
        bd=5,insertwidth=2,
        width=14, borderwidth=4,
        relief=tk.RIDGE)
    entry.grid(columnspan=4, padx=10, pady=10)

    button_conf = {'padx': 10, 'pady': 10,
            'font': ('Helvetica', 14),
            'bg': 'black', 'fg': 'white',
            'relief': tk.RAISED, 'bd': 2}

    buttons = [
        ('7', 1, 0), ('8', 1, 1),
        ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), 
        ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), 
        ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), 
        ('=', 4, 2), ('+', 4, 3)
    ]

    for (text, row, col) in buttons:
        action = {
            '=': equalpress, 'C': clear
            }.get(
            text, lambda t=text: press(t))
        tk.Button(root, text=text,
            command=action, **button_conf
            ).grid(row=row,
                column=col, sticky="nsew")

    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i+1, weight=1)

    root.mainloop()
