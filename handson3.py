import tkinter as tk

def add():
    a = float(entry1.get())
    b = float(entry2.get())
    result.config(text="Result: " + str(a + b))

def subtract():
    a = float(entry1.get())
    b = float(entry2.get())
    result.config(text="Result: " + str(a - b))

def multiply():
    a = float(entry1.get())
    b = float(entry2.get())
    result.config(text="Result: " + str(a * b))

def divide():
    a = float(entry1.get())
    b = float(entry2.get())
    if b == 0:
        result.config(text="Cannot divide by 0")
    else:
        result.config(text="Result: " + str(a / b))

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x230")
root.configure(bg="lightgreen")

title = tk.Label(root, text="Ano solve tayo?", bg="white")
title.pack(pady=5)

label1 = tk.Label(root, text="Enter 1st Number:", bg="lightgreen")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter 2nd Number:", bg="lightgreen")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

frame = tk.Frame(root, bg="lightgreen")
frame.pack(pady=10)

miles_add = tk.Button(frame, text="Add", width=10, command=add)
miles_add.grid(row=0, column=0, padx=5, pady=5)

miles_sub = tk.Button(frame, text="Subtract", width=10, command=subtract)
miles_sub.grid(row=0, column=1, padx=5, pady=5)

miles_mul = tk.Button(frame, text="Multiply", width=10, command=multiply)
miles_mul.grid(row=1, column=0, padx=5, pady=5)

miles_div = tk.Button(frame, text="Division", width=10, command=divide)
miles_div.grid(row=1, column=1, padx=5, pady=5)

result = tk.Label(root, text="Result:", bg="lightgreen", font=("Arial", 12))
result.pack()

root.mainloop()

