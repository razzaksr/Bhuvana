from cgitb import text
from ctypes import resize
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from pymysql import *

class Fresh(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("New Corporate")
        self.geometry("700x550")
        self.configure(background='pink')
        self.resizable(False,False)
        
        self.head=Label(self,text="MOU With New Corporate",font=("Times New Roman",28),fg='white',bg='pink').place(x=180,y=10)
        #self.head.grid(row=0,column=1)
        
        self.lb1=Label(self,text="The Corporate name",font=("Times New Roman",20),fg="white",bg='pink').place(x=50,y=100)
        self.lb2=Label(self,text="The Corporate nature",font=("Times New Roman",20),fg="white",bg='pink').place(x=50,y=150)
        self.lb3=Label(self,text="The Corporate opennings",font=("Times New Roman",20),fg="white",bg='pink').place(x=50,y=200)
        self.lb4=Label(self,text="The Corporate place",font=("Times New Roman",20),fg="white",bg='pink').place(x=50,y=250)
        self.lb5=Label(self,text="The Corporate total employees",font=("Times New Roman",20),fg="white",bg='pink').place(x=50,y=300)
        self.lb6=Label(self,text="The Corporate minimum salary",font=("Times New Roman",20),fg="white",bg='pink').place(x=50,y=350)
        self.lb7=Label(self,text="The Corporate ratings",font=("Times New Roman",20),fg="white",bg='pink').place(x=50,y=400)
        
        self.e1=Entry(self,font=("Times New Roman",18),fg='white',bg='pink').place(x=400,y=100)
        self.cb=Combobox(self,font=("Times New Roman",17),values=("Product","Service","BPO","Marketting")).place(x=400,y=150)
        
        self.cb1v=StringVar()
        self.cb1v.set("Java")
        self.cb2v=StringVar()
        self.cb2v.set("Java script")
        self.cb3v=StringVar()
        self.cb3v.set("Python")
        
        self.cb1=Checkbutton(self,var=self.cb1v,text="Java Developer").place(x=250,y=230)
        self.cb2=Checkbutton(self,var=self.cb2v,text="Java script Developer").place(x=360,y=230)
        self.cb3=Checkbutton(self,var=self.cb3v,text="Python Developer").place(x=500,y=230)
        
        self.e2=Entry(self,font=("Times New Roman",18),fg='white',bg='pink').place(x=400,y=260)
        self.e3=Entry(self,font=("Times New Roman",18),fg='white',bg='pink').place(x=400,y=300)
        self.e4=Entry(self,font=("Times New Roman",18),fg='white',bg='pink').place(x=400,y=350)
        self.e5=Entry(self,font=("Times New Roman",18),fg='white',bg='pink').place(x=400,y=400)
        
        self.b1=Button(self,text="Approve",fg='white',bg='pink',font=("Times New Roman",18),command=self.submit).place(x=210,y=460)
        self.b2=Button(self,text="Cancel",fg='white',bg='pink',font=("Times New Roman",18),command=self.reset).place(x=400,y=460)
    
    def submit(self):
        messagebox.showinfo("Approve","Corporate yet to be added")
        con=connect(host='localhost',user='root',password='',database='bhuvana')
        
        qry="""insert into corporate(org,nature,opennings,place,employees,basic,ratings) values('%s','%s','%s','%s','%d','%f','%f')"""%(str(self.e1.get()),self.cb.get(),)
        
        con.close()
    
    def reset(self):
        messagebox.showinfo("Cancel","All fields yet to be cleared ")

f=Fresh()
f.mainloop()