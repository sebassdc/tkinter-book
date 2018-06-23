from tkinter import Tk, Label, Button

root = Tk()
label = Label(root, text="This is a label widget")
button = Button(root, text="This is a button widget")
label.pack()
button.pack()
root.mainloop()