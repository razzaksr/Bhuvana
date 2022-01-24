# Combobox

from tkinter import *
from tkinter.ttk import Combobox


class MyCombo(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Combobox demonstration")
        self.geometry('600x300')
        
        self.cmb=Combobox(self)
        self.cmb.grid(row=0,column=0)
        self.cmb['values']=['Web developer','Web designer','Automation tester','Manual tester']
        
        self.bt=Button(self,text="Select Role",command=self.hai)
        self.bt.grid(row=1,column=0)
        
        self.lb=Label(self,text="User has choosen: ")
        self.lb.grid(row=2,column=0)
    
    def hai(self):
        tmp=self.cmb.get()
        self.lb.config(text=tmp+" has choosen")
        
my=MyCombo()
my.mainloop()