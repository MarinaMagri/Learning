# from tkinter import *


# root = Tk()
# root.title("Application")
# root.geometry("640x480")
# root.resizable(width = False, height = False)


# cnt = 0 

# def Clicked():
#     global cnt
#     cnt +=1
#     print(f"{cnt} clicks")

# button = Button(
#     text = "button",
#     width = 20,
#     height = 10,
#     background = "yellow",
#     foreground = "red",
#     font = ("Verdana", "24"),
#     command = Clicked
# )
# button.pack()

# button2 = Button(
#     text = "button 2"
# )
# button2.pack()

# if __name__ == "__main__":
#     root.mainloop()
# 

from sre_constants import JUMP
from tkinter import *
from turtle import back


root = Tk()
root.title("Application")
root.geometry("640x480")
root.resizable(width = False, height = False)

# button = Button(
#     text = "123"
# )

# button1 = Button(
#     text = "321"
# )

# button2 = Button(
#     text = "456"
# )


# button.grid(
#     row = 0,
#     column = 1
# )

# button1.grid(
#     row = 1,
#     column = 0
# )

# label = Label(
#     text = "Click on the button",
# )
# button = Button(
#     text = "Here"
# )
# label.pack()
# button.pack()

# button.place(
#     width = 250,
#     height = 200,
#     x = 200,
#     y = 150
# )


entry = Entry(
    width = 20,
    font = ("Times New Roman", 18),
    justify = CENTER,
    # show = "&"
)


def clicked():
    s = entry.get()
    print(s)

def delete_text():
    entry.delete(0, END)


button = Button(
    text = "Click here",
    command = clicked
)
button2 = Button(
    text = "Delete",
    command = delete_text
)

entry.pack()
button.pack()
button2.pack()

if __name__ == "__main__":
    root.mainloop()

