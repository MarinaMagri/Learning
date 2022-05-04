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


from tkinter import *


root = Tk()
root.title("Aplication")
root.geometry("640x480")
root.resizable(width = False, height = False)


button = Button(
text = "123"
)
button.pack()



if __name__ == "__main__" :
    root.mainloop