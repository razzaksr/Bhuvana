from tkinter import *

obj=Tk()
obj.geometry('600x300')
obj.title("Second window")

#hai=Label(obj,text="My first label as component",font=("Times New Roman",24),fg='blue',bg='black').place(x=100,y=200)
hai=Label(obj,text="My first label as component",font=("Times New Roman",24),fg='blue',bg='black')
hi=Label(obj,text="My second label as component",font=("Times New Roman",24),fg='blue',bg='black')
#hai.pack(padx=0,pady=0,side=TOP,fill='both')
hai.grid(row=0,column=0)
hi.grid(row=0,column=1)

obj.mainloop()