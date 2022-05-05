from argparse import Action
from tkinter import *

from numpy import equal

root = Tk()
root.title("Application")
root.geometry("640x480")
root.resizable(width = False, height = False)

action = ""
value = 0

entry = Entry(
    width = 25,
    font = ("Times New Roman", 18)
)
def plus_function():
    global value
    global action
    value = float(entry.get())
    action = "+"
#     print(f"Action +, Value {entry.get()} ")
    entry.delete(0, END)
#     return print(f"{entry.get()} + ")
# get_summ = lambda a,b: a+b

def equal_function():
    global value
    global action
    if action == "+":
        value += float(entry.get())
    if action == "-":
        value -= float(entry.get())
    if action == "/":
        value /= float(entry.get())
    if action == "*":
        value *= float(entry.get())
    print(value)

def minus_function():
    global value
    global action
    value = float(entry.get())
    action = "-"
    entry.delete(0, END)

def division_function():
    global value
    global action
    value = float(entry.get())
    action = "/"
    entry.delete(0, END)

def multiply_function():
    global value
    global action
    value = float(entry.get())
    action = "*"
    entry.delete(0, END)

button_plus = Button(
    text = "+",
    command = plus_function
)
button_equal = Button(
    text = "=",
    command = equal_function
)
button_minus = Button(
    text = "-",
    command = minus_function
)
button_division = Button(
    text = "/",
    command = division_function
)
button_multiply= Button(
    text = "*",
    command = multiply_function
)

entry.pack()
button_plus.pack()
button_equal.pack()
button_minus.pack()
button_division.pack()
button_multiply.pack()


if __name__ == "__main__":
    root.mainloop()

