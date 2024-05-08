import tkinter as tk
from tkinter import messagebox

def say_hello():
    messagebox.showinfo("Message", "Hello World")

root = tk.Tk()
button = tk.Button(root, text="Click me", command=say_hello)
button.pack()

root.mainloop()