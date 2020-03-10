from tkinter import *

window = Tk()
window.title=("Frames")

frame=Frame(window,height=200,width=400,bg='red',bd='3',relief=SUNKEN)
frame.pack(fill=X)
button1=Button(frame,text="Butt1")
button1.pack(side=LEFT,padx=20,pady=20)
button2=Button(frame,text="Butt2")
button2.pack(side=RIGHT,padx=20,pady=20)


searchbar=LabelFrame(window,text='Search Bar',bg='yellow')
searchbar.pack(side=TOP,padx=50,pady=50)
lbl=Label(searchbar,text='Search',bg='yellow')
lbl.pack(side=LEFT,padx=20,pady=15)
entry=Entry(searchbar)
entry.pack(side=LEFT,padx=20,pady=15)
sbut=Button(searchbar,text='Search')
sbut.pack(side=RIGHT,padx=10)


window.geometry("600x600+450+250")
window.mainloop()
