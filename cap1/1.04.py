import tkinter as tk
from tkinter import Frame, Button, Label
root = tk.Tk()

frame = Frame(root)
Label(frame, text = "Pack demo of side and fill").pack()
Button(frame, text = "A").pack(side = tk.LEFT, fill = tk.Y)
Button(frame, text = "B").pack(side = tk.TOP, fill = tk.X)
Button(frame, text = "C").pack(side = tk.RIGHT, fill = tk.NONE)
Button(frame, text = "D").pack(side = tk.TOP, fill = tk.BOTH )
frame.pack()

Label(root, text="Pack demo of expand").pack()
Button(root, text="I do not expand").pack()
Button(root, text="I do not fill x but i expand").pack(expand = 1)
Button(root, text="I fill x and expand").pack(fill=tk.X, expand = 1)


root.mainloop()