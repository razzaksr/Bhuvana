from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import messagebox

class Small(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Small items")
        self.geometry('500x300')
        
        self.b1=BooleanVar(False)
        self.b2=BooleanVar(False)
        self.b3=BooleanVar(False)
        
        self.cb1=Checkbutton(self,variable=self.b1,text='Falooda')
        self.cb1.grid(row=0,column=0)
        
        self.cb2=Checkbutton(self,variable=self.b2,text='CashewShake')
        self.cb2.grid(row=1,column=0)
        
        self.cb3=Checkbutton(self,variable=self.b3,text='Coke')
        self.cb3.grid(row=2,column=0)
        
        self.bt=Button(self,text="Order",command=self.place)
        self.bt.grid(row=3,column=0)
    
        self.radioVar=StringVar()
        self.radioVar.set("")
        
        self.rb1=Radiobutton(self,variable=self.radioVar,value="card",text="Card Payment",command=self.order)
        self.rb1.grid(row=4,column=1)
        
        self.rb2=Radiobutton(self,variable=self.radioVar,value="cash",text="Cash Payment",command=self.order)
        self.rb2.grid(row=5,column=1)
        
        self.rb3=Radiobutton(self,variable=self.radioVar,value="upi",text="UPI Payment",command=self.order)
        self.rb3.grid(row=6,column=1)
    
    def place(self):
        messagebox.showinfo(self,"You placed "+format(self.b1.get())+" "+format(self.b2.get())+" "+format(self.b3.get()))
    
    def order(self):
        messagebox.showinfo("My Order Mode",str(self.radioVar.get()))
        
        
        
sm=Small()
sm.mainloop()