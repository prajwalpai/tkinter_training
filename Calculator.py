from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Pai Calculator")


##############################  Functions
def input_number(x):
    if entry_box.get() == "O":
        entry_box.delete(0, END)
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


def input_operator(x):
    if entry_box.get() != "O":
        length = len(entry_box.get())
        entry_box.insert(length, button_operator[x]['text'])

def input_clear():
    if entry_box.get() != "O":
        entry_box.delete(0,END)
        entry_box.insert(0, "O")

def input_back():
        lenght=len(entry_box.get())
        entry_box.delete(lenght - 1, END)
        if lenght == 1:
            entry_box.insert(0,"O")

def input_equal():
    result = eval(entry_box.get())
    entry_box.delete(0, END)
    entry_box.insert(0,result)



##############################  Entry Box
entry_box = Entry(font='verdana 14 bold', width=22, bd=5, justify=RIGHT, bg='#42f566')
entry_box.insert(0, "O")
entry_box.place(x=20, y=10)

##############################  Number Buttons
button_number = []
for i in range(10):
    button_number.append(Button(window, text=str(i), width='5', font='Times 15 bold',
                                command=lambda x=i: input_number(x)))

btn_num = 1
for i in range(0, 3):
    for j in range(0, 3):
        button_number[btn_num].place(x=21 + i * 70, y=60 + j * 50)
        btn_num = btn_num + 1

##############################  Operator Buttons

button_operator = []
for i in range(4):
    button_operator.append(Button(window, width='5',highlightbackground='orange', font='Times 15 bold',
                                command=lambda x=i: input_operator(x)))

for i in range(4):
    button_operator[i].place(x=230,y=60 + i * 50)

button_operator[0]['text']="+"
button_operator[1]['text']="-"
button_operator[2]['text']="*"
button_operator[3]['text']="/"

##############################  Other special buttons

button_zero=Button(window,text="0",width='23', font='Times 15 bold',command= lambda x=0:input_number(x)).place(x=21,y=210)
button_point=Button(window,text=".",width='5',highlightbackground='orange', font='Times 15 bold',command= lambda x=".":input_number(x)).place(x=21,y=260)
button_clear=Button(window,text="c",width='5',highlightbackground='orange', font='Times 15 bold',command= lambda x=0:input_clear()).place(x=90,y=260)
button_back=Button(window,text="<",width='5',highlightbackground='orange', font='Times 15 bold',command= lambda x=0:input_back()).place(x=160,y=260)
button_equal=Button(window,text="=",width='5',highlightbackground='red', font='Times 15 bold',command= lambda x=0:input_equal()).place(x=230,y=260)


window.geometry("300x330+400+400")
window.mainloop()
