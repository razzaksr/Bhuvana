from tkinter import *
from pymysql import *

class Fresh(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("New Corporate")
        self.geometry("700x500")
        self.configure(background='pink')
        
        self.head=Label(self,text="MU With New Corporate",font=("Times New Roman",28),fg='white',bg='pink').place(x=180,y=10)
        #self.head.grid(row=0,column=1)

f=Fresh()
f.mainloop()