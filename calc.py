import tkinter as tk

def on_click(button_text):
    entry.insert(tk.END, button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

app = tk.Tk()
app.title("Calculator")

entry = tk.Entry(app, width=20, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    action = lambda x=text: on_click(x) if x != '=' else calculate()
    tk.Button(app, text=text, width=5, height=2, command=action).grid(row=row, column=col, padx=5, pady=5)

tk.Button(app, text="C", width=5, height=2, command=clear).grid(row=5, column=0, columnspan=4, pady=5, sticky="we")

app.mainloop()
