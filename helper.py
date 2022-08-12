from tkinter import *
racc=Tk()
racc.geometry("400x150")
racc.title("Accuracy of Result")
lab=Label(racc,text="Accuracy of this result\n",font=(20))
lab.place(relx=0.29,rely=0.25)
lal=Label(racc,text=str((1/3)*100),font=(20))
lal.place(relx=0.3,rely=0.45)

