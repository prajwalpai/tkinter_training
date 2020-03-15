from tkinter import *
from tkinter import ttk
window=Tk()

progbar=ttk.Progressbar(window,length='200')
progbar.pack(pady=20)

window.geometry("600x600+450+250")
window.mainloop()