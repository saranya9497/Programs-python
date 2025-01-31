import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime("%H:%M:%S %p")
    label.config(text=time_string)
    label.after(1000, update_time)

app = tk.Tk()
app.title("Digital Clock")

label = tk.Label(app, font=("Arial", 40), bg="black", fg="white")
label.pack(padx=20, pady=20)

update_time()

app.mainloop()
