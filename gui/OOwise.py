from tkinter import *
from tkinter import messagebox

class Annalili(Tk):
    def __init__(self):
        Tk.__init__(self) # inorder work your init quite like tk init
        self.title("My first class oriented window")
        self.geometry('500x200')
        
        self.hey=Button(self,text="Click ME!",fg='red',bg='black',command=self.yet)
        self.hey.grid(row=0,column=0)
    
    def yet(self):
        #print("Button clicked now")
        messagebox.showinfo(self,"Button clicked now")

an=Annalili()
an.mainloop()