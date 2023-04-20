from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x100")
window.title("Button App")

lbl = Label(window, text="Click a Button")
lbl.pack()

msg_warning = "This is a WARNING Message"
def warning():
    messagebox.showwarning("Warning", msg_warning)

btn_warn = Button(window, text="Warning Info", command=warning)
btn_warn.pack()

btn_close = Button(window, text="Exit", command=window.destroy)
btn_close.pack()

window.mainloop()
