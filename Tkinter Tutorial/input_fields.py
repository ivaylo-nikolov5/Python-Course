from tkinter import *

root = Tk()

e = Entry(root, width=45, fg="white", bg="black", borderwidth=6)
e.pack()
e.insert(0, "Enter your name!: ")


def my_click():
    hello = f"Hello, {e.get()}!"
    my_label = Label(root, text=hello, fg="red")
    my_label.pack()


myButton = Button(root, text="Enter your name!", command=my_click, fg="red", bg="grey")
myButton.pack()

root.mainloop()