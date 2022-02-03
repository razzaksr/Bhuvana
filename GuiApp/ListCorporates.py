from tkinter import messagebox
from pymysql import *
from tkinter import *

class Available(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Listing all corporates")
        self.geometry("500x300")
        
        con=connect(host="localhost",user="root",password="",database="bhuvana")
        
        qry="select * from corporate"
        
        cur=con.cursor()
        
        cur.execute(qry)
        
        all = cur.fetchall() # extract all the fields
        
        self.h1=Entry(self,width=33)
        self.h1.insert(END,"Organisation Name")
        self.h1.configure(justify=CENTER)
        self.h1.grid(row=0,column=0)
        
        self.h2=Entry(self,width=33)
        self.h2.configure(justify=CENTER)
        self.h2.insert(END,"Organisation Nature")
        self.h2.grid(row=0,column=1)
        
        self.h3=Entry(self,width=33)
        self.h3.configure(justify=CENTER)
        self.h3.insert(END,"Organisation Opennings")
        self.h3.grid(row=0,column=2)
        
        self.h4=Entry(self,width=33)
        self.h4.configure(justify=CENTER)
        self.h4.insert(END,"Organisation Locations")
        self.h4.grid(row=0,column=3)
        
        self.h5=Entry(self,width=33)
        self.h5.configure(justify=CENTER)
        self.h5.insert(END,"Organisation Resources count")
        self.h5.grid(row=0,column=4)
        
        self.h6=Entry(self,width=33)
        self.h6.configure(justify=CENTER)
        self.h6.insert(END,"Organisation Basic Salary")
        self.h6.grid(row=0,column=5)
        
        self.h7=Entry(self,width=33)
        self.h7.configure(justify=CENTER)
        self.h7.insert(END,"Organisation Rating")
        self.h7.grid(row=0,column=6)
        
        self.h8=Entry(self)
        self.h8.configure(justify=CENTER)
        self.h8.insert(END,"Actions")
        self.h8.grid(row=0,column=7)
        
        self.users=""
        
        line=1
        for row in all:
            for col in range(0,7):
                self.data=Entry(self,width=33)
                self.data.configure(justify=CENTER)
                self.data.insert(END,row[col])
                self.data.grid(row=line,column=col)
            self.ed=Button(self,text="Edit",command=self.toSend)
            self.ed.grid(row=line,column=7)
            line+=1
        
        con.close()
    
    def toSend(self,hai):
        messagebox.showinfo("Edit","Edit called "+hai)
        

a=Available()
a.mainloop()