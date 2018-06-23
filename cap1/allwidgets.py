import tkinter as tk

root = tk.Tk()

v = "thing"

# menu
menu_bar = tk.Frame(root)
menu_bar.pack()
tk.Menubutton(menu_bar).pack()
tk.Menu(menu_bar)


# frame
frame = tk.Frame(root)
frame.pack()

tk.Label(frame).pack()
tk.Entry(frame).pack()
tk.Button(frame).pack()
tk.Checkbutton(frame).pack()
tk.Radiobutton(frame).pack()
tk.OptionMenu(frame, variable=v, value="Apple").pack()
# tk.Bitmapclass(frame).pack()

# frame2

frame2 = tk.Frame(root)
frame2.pack()

# tk.ImageClass(frame2).pack()
tk.Listbox(frame2).pack()
tk.Spinbox(frame2).pack()
tk.Scale(frame2).pack()
tk.LabelFrame(frame2).pack()
tk.Message(frame2).pack()

# frame3

frame3 = tk.Frame(root)
frame3.pack()

tk.Text(frame3).pack()
tk.Scrollbar(frame3).pack()

# frame4

frame4 = tk.Frame(root)
frame4.pack()

tk.Canvas(frame4).pack()
tk.PanedWindow(frame4).pack()

label = tk.Label(root, text="This is a label widget")
button = tk.Button(root, text="This is a button widget")
label.pack()
button.pack()
root.mainloop()