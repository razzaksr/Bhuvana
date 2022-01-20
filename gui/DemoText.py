from tkinter import *
from tkinter import messagebox

class Texting(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Text box window")
        self.geometry('500x200')
        
        self.myStyle = font=('Times New Roman',14,'bold')
        
        self.ph=PhotoImage(file='D:\\Course backups\\Python\\Bhuvana\\gui\\jd.ico')
        self.iconphoto(False,self.ph)
        
        self.hai=Entry(self,width=20,fg='white',bg='blue',font=self.myStyle)
        self.hai.grid(row=0,column=0)
        
        self.hey=Button(self,text="Find Out",font=self.myStyle,fg='red',bg='blue',command=self.goOn)
        self.hey.grid(row=1,column=0)
    def goOn(self):
        messagebox.showinfo(self,str(self.hai.get()))

tx=Texting()
tx.mainloop()