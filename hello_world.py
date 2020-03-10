from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window=Tk()
window.title("Hello World!")

def callback1():
    msgbox1= messagebox.showinfo("Changing view!","The title will be RED")
    window.geometry("510x510")
    label.config(text='This is the Window Name!',fg='red',font="Ariel 21")

def callback2():
    msgbox2 = messagebox.showwarning("Changing the view Again!","The title will be GREEN")
    window.geometry("490x490")
    label.config(text='That is the name of this Window!',fg='green',font="Times 19")

def callback3():
    user_name=userid.get()
    passw=passwd.get()
    print(f"The user is {user_name} with password being {passw} with 'remember me' option : {chvar.get()} and gender is {gender.get()} and month being {months.get()}")

label=Label(window,text='This is default Window Name')
button1=Button(window,text="Plain view",command=callback1)
button2=ttk.Button(window,text="Fancy View",command=callback2)
usr_label=Label(window,text="Enter Username: ")
passwd_label=Label(window,text="Enter Password :")

userid= ttk.Entry(window,width=30)

passwd= ttk.Entry(window,width=30)
passwd.config(show='*')

button3=ttk.Button(window,text="login",command=callback3)

chvar = IntVar()
chvar.set(0)
cbox=Checkbutton(window,text="Remember me",variable=chvar,font="Arial 16")
gender = StringVar()
ttk.Radiobutton(window,text='male',value='male',var=gender).place(x=150,y=300)
ttk.Radiobutton(window,text='female',value='female',var=gender).place(x=300,y=300)
months=StringVar()
allmonths=["Jan","Feb","Mar","Apr","May","Jun","Jul",'Aug']
combobox=ttk.Combobox(window,textvariable=months,values=(allmonths),state='readonly').place(x=50,y=325)

year = StringVar()
Spinbox(window,from_=1981,to=2010,textvariable=year,state='readonly').place(x=250,y=325)

textedtr = Text(window,width=55,height=6)

textedtr.insert(INSERT,"Testing what appears")

label.place(x=140,y=20)
button1.place(x=50,y=60)
button2.place(x=350,y=60)
usr_label.place(x=50,y=150)
userid.place(x=180,y=150)
passwd_label.place(x=50,y=190)
passwd.place(x=180,y=190)
cbox.place(x=180,y=220)
button3.place(x=240,y=260)
textedtr.place(x=50,y=370)


window.geometry("500x500+550+300")
window.mainloop()
