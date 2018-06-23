from tkinter import Frame, Button, Tk
root = Tk()

parent = Frame(root)
# TOP-DOWN
Button(parent, text = "ALL IS WELL").pack(fill='x')
Button(parent, text = "BACK TO BASICS").pack(fill='x')
Button(parent, text = "CATCH ME IF YOU CAN").pack(fill='x')

# SIDE BY SIDE
Button(parent, text = "LEFT").pack(side='left')
Button(parent, text = "CENTER").pack(side='left')
Button(parent, text = "RIGHT").pack(side='left')

parent.pack()


root.mainloop()