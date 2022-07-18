from tkinter import *

root = Tk()


def my_click():
    my_label = Label(root, text="Look! I clicked a button!!!", fg="red")
    my_label.pack()


myButton = Button(root, text="Click me!", command=my_click, fg="red", bg="grey")
myButton.pack()

root.mainloop()