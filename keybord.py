import tkinter as tk

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("لوحة مفاتيح")
root.geometry("550x550")

# إضافة حقل إدخال نص
entry = tk.Entry(root, width=50, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=10, pady=10)

# دالة لإضافة الحرف المضغوط إلى حقل الإدخال
def press_key(event):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + event.widget.cget("text"))

# دالة لحذف آخر حرف في حقل الإدخال
def delete_key(event):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

# الحروف على لوحة المفاتيح
keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
    ['Space', 'Delete']
]

# إضافة الأزرار إلى النافذة
for i, row in enumerate(keys):
    for j, key in enumerate(row):
        if key == 'Space':
            button = tk.Button(root, text='Space', width=30, height=2, bg='black', fg='white')
            button.grid(row=i + 1, column=0, columnspan=7)
            button.bind("<Button-1>", press_key)
        elif key == 'Delete':
            button = tk.Button(root, text='←', width=15, height=2, bg='black', fg='white')
            button.grid(row=i + 1, column=7, columnspan=3)
            button.bind("<Button-1>", delete_key)
        else:
            button = tk.Button(root, text=key, width=5, height=2, bg='black', fg='white')
            button.grid(row=i + 1, column=j)
            button.bind("<Button-1>", press_key)

# تشغيل الحلقة الرئيسية للتطبيق
root.mainloop()
