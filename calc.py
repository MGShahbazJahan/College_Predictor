from tkinter import *
root=Tk()
root.title("simple calculator")
root.configure(background="black")
def button_click(number):
    c=e.get()
    e.delete(0,END)
    e.insert(0,str(c)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    f=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="addition"
    f_num=int(f)
def button_sub():
    f=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="subtraction"
    f_num=int(f)
def button_mul():
    f=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="multiply"
    f_num=int(f)
def button_div():
    f=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="divide"
    f_num=int(f)
def button_equal():
    s=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(s))
    if math=="subtraction":
        e.insert(0,f_num-int(s))
    if math=="multiply":
        e.insert(0,f_num*int(s))
    if math=="divide":
        e.insert(0,f_num/int(s))
e=Entry(root,width=60,borderwidth=10)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
button_0=Button(root,text="0",padx=102,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(0))
button_1=Button(root,text="1",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,fg="white",bg="grey",font=("arial",20,"bold"),command=lambda: button_click(9))
button_add=Button(root,text="+",padx=38,pady=68,fg="green",bg="grey",font=("arial",20,"bold"),command=button_add)
button_sub=Button(root,text="-",padx=41,pady=20,fg="green",bg="grey",font=("arial",20,"bold"),command=button_sub)
button_mul=Button(root,text="*",padx=40,pady=20,fg="green",bg="grey",font=("arial",20,"bold"),command=button_mul)
button_div=Button(root,text="/",padx=44,pady=20,fg="green",bg="grey",font=("arial",20,"bold"),command=button_div)
button_equal=Button(root,text="=",padx=100,pady=20,fg="white",bg="green",font=("arial",20,"bold"),command=button_equal)
button_clear=Button(root,text="clear",padx=76,pady=20,fg="red",bg="grey",font=("arial",20,"bold"),command=button_clear)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_0.grid(row=5,column=0,columnspan=2)
button_add.grid(row=3,column=3,rowspan=2)
button_sub.grid(row=2,column=3)
button_mul.grid(row=1,column=3)
button_div.grid(row=1,column=2)
button_equal.grid(row=5,column=2,columnspan=2)
button_clear.grid(row=1,column=0,columnspan=2)
root.mainloop()

