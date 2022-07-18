from tkinter import *

root = Tk()

label = Label(root, text="Hello World!")
label2 = Label(root, text="My name is Ivailo!")
label3 = Label(root, text=" ")

label.grid(row=0, column=0)
label2.grid(row=1, column=5)
label3.grid(row=1, column=1)

root.mainloop()