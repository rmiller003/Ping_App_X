from tkinter import *

window = Tk()
window.wm_geometry("400x50")
window.title("Tkinter App X")

lbl = Label(window, text="Hello World")
lbl.pack()

window.mainloop()
