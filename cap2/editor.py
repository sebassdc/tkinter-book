import tkinter as tk

PROGRAM_NAME = " Footprint Editor "

root = tk.Tk()
root.title(PROGRAM_NAME)

# MENU CODE
menu_bar = tk.Menu(root)

# File
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)

# Edit
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

# View
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view_menu)

# About
about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)



root.config(menu=menu_bar)

root.mainloop()