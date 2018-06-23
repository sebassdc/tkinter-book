import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Click at different\n locations in the frame bellow").pack()

def callback(event):
    print(dir(event))
    print("You clicked at", event.x, event.y)

frame = tk.Frame(root, bg='khaki', width=130, height=80)
frame.bind("<Button-1>", callback)
frame.pack()


root.mainloop()