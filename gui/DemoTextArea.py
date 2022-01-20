from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class Area(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Python text area")
        self.geometry('500x300')
        
        self.big=ScrolledText(self)
        self.big.grid(row=0,column=0)
        self.hey=Button(self,text="Find Out",font=('Arial',20),fg='red',bg='blue',command=self.goOn)
        self.hey.grid(row=2,column=0)
        
        self.swap=Spinbox(self,from_=50,to=100)
        self.swap.grid(row=1,column=0)
        
    def goOn(self):
        messagebox.showinfo(self,str(self.big.get(0.1,END))+str(self.swap.get()))

a=Area()
a.mainloop()