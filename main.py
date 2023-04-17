from tkinter import *

window = Tk()
window.wm_geometry("400x50")
window.title("Tkinter App X")

lbl_1 = Label(window, text="Default Formatting")
lbl_1.pack()

lbl_2 = Label(window, text="Red Text", fg="red")
lbl_2.pack()

lbl_3 = Label(window, text="RAISED BLUE Text", fg="blue", relief="raised")
lbl_3.pack()

lbl_4 = Label(window, text="Text with Yellow Background", bg="yellow")
lbl_4.pack()

window.mainloop()
