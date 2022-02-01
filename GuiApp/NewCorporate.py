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
        self.geometry("700x450")
        self.configure(background='pink')
        self.resizable(False,False)
        
        self.head=Label(self,text="MOU With New Corporate",font=("Times New Roman",28),fg='white',bg='pink')#.place(x=180,y=10)
        self.head.grid(row=0,column=0)
        
        self.lb1=Label(self,text="The Corporate name",font=("Times New Roman",20),fg="white",bg='pink')#.place(x=50,y=100)
        self.lb1.grid(row=1,column=0)
        self.lb2=Label(self,text="The Corporate nature",font=("Times New Roman",20),fg="white",bg='pink')#.place(x=50,y=150)
        self.lb2.grid(row=2,column=0)
        self.lb3=Label(self,text="The Corporate opennings",font=("Times New Roman",20),fg="white",bg='pink')#.place(x=50,y=200)
        self.lb3.grid(row=3,column=0)
        self.lb4=Label(self,text="The Corporate place",font=("Times New Roman",20),fg="white",bg='pink')#.place(x=50,y=250)
        self.lb4.grid(row=4,column=0)
        self.lb5=Label(self,text="The Corporate total employees",font=("Times New Roman",20),fg="white",bg='pink')#.place(x=50,y=300)
        self.lb5.grid(row=5,column=0)
        self.lb6=Label(self,text="The Corporate minimum salary",font=("Times New Roman",20),fg="white",bg='pink')#.place(x=50,y=350)
        self.lb6.grid(row=6,column=0)
        self.lb7=Label(self,text="The Corporate ratings",font=("Times New Roman",20),fg="white",bg='pink')#.place(x=50,y=400)
        self.lb7.grid(row=7,column=0)
        
        self.e1=Entry(self,font=("Times New Roman",18),fg='white',bg='pink')##.place(x=400,y=100)
        self.e1.grid(row=1,column=1)
        self.cb=Combobox(self,font=("Times New Roman",17),values=("Product","Service","BPO","Marketting"))#.place(x=400,y=150)
        self.cb.grid(row=2,column=1)
        self.cb1v=BooleanVar(False)#StringVar()
        #self.cb1v.set("Java")
        self.cb2v=BooleanVar(False)#StringVar()
        #self.cb2v.set("Java script")
        self.cb3v=BooleanVar(False)#StringVar()
        #self.cb3v.set("Python")
        
        self.cb1=Checkbutton(self,var=self.cb1v,text="Java").place(x=400,y=130)
        #self.cb1.grid(row=3,column=0)
        self.cb2=Checkbutton(self,var=self.cb2v,text="Java script").place(x=470,y=130)
        #self.cb1.grid(row=3,column=1)
        self.cb3=Checkbutton(self,var=self.cb3v,text="Python").place(x=580,y=130)
        #self.cb1.grid(row=3,column=2)
        
        self.e2=Entry(self,font=("Times New Roman",18),fg='white',bg='pink')#.place(x=400,y=260)
        self.e2.grid(row=4,column=1)
        self.e3=Entry(self,font=("Times New Roman",18),fg='white',bg='pink')#.place(x=400,y=300)
        self.e3.grid(row=5,column=1)
        self.e4=Entry(self,font=("Times New Roman",18),fg='white',bg='pink')#.place(x=400,y=350)
        self.e4.grid(row=6,column=1)
        self.e5=Entry(self,font=("Times New Roman",18),fg='white',bg='pink')#.place(x=400,y=400)
        self.e5.grid(row=7,column=1)
        
        self.b1=Button(self,text="Approve",fg='white',bg='pink',font=("Times New Roman",18),command=self.submit).place(x=210,y=330)
        
        self.b2=Button(self,text="Cancel",fg='white',bg='pink',font=("Times New Roman",18),command=self.reset).place(x=400,y=330)
        
    
    def submit(self):
        messagebox.showinfo("Approve","Corporate yet to be added "+str(self.e1.get()))
        con=connect(host='localhost',user='root',password='',database='bhuvana')
        
        con.autocommit(True)
        
        tmp=""
        
        if format(self.cb1v.get())==True:
            tmp+="Java,"
        if format(self.cb2v.get())==True:
            tmp+="Javascript,"
        if format(self.cb3v.get())==True:
            tmp+="Python,"
        
        count=int(str(self.e3.get()))
        basi=float(str(self.e4.get()))
        rate=float(str(self.e5.get()))
        
        qry="""insert into corporate(org,nature,opennings,place,employees,basic,ratings) values('%s','%s','%s','%s','%d','%f','%f')"""%(str(self.e1.get()),self.cb.get(),tmp,str(self.e2.get()),count,basi,rate)
        
        cur=con.cursor()
        
        ack = cur.execute(qry)
        
        if ack!=0:
            messagebox.showinfo("Alert","Corporate has inserted")
        else:
            messagebox.showinfo("Alert","Corporate hasn't inserted")
        
        con.close()
    
    def reset(self):
        messagebox.showinfo("Cancel","All fields yet to be cleared ")
        self.e1.insert(1.0,"")
        self.e2.insert(1.0,"")
        self.e3.insert(1.0,"")
        self.e4.insert(1.0,"")
        self.e5.insert(1.0,"")
        self.cb1v.set(False)
        self.cb2v.set(False)
        self.cb3v.set(False)
        self.cb.selection_clear()
        

f=Fresh()
f.mainloop()