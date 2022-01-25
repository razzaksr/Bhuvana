# menu and actions

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.scrolledtext import ScrolledText


class Editor(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Sample Editor")
        self.geometry("500x300")
        
        #menu bar
        self.bar=Menu(self)
        #menu allocation
        self.m1=Menu(self.bar,tearoff=0)
        
        self.m1.add_command(label="Open",command=self.openning)
        self.m1.add_command(label="Save",command=self.saving)
        self.m1.add_command(label="Exit",command=self.finish)
        
        self.bar.add_cascade(label="File",menu=self.m1)
        
        self.config(menu=self.bar)
        
        self.area=ScrolledText(self)
        self.area.pack(expand=True,fill=BOTH)
    
    def finish(self):
        self.destroy()
    
    def openning(self):
        messagebox.showinfo("Open File","File Open process initiated")
        which=askopenfile(mode="r",filetypes=[
            ('All Files','*.*'),
            ('Java Files','*.java'),
            ('Python Files','*.py')
            ])
        if which is not None:
            contents=which.read()
            self.area.insert(1.0,contents)
            messagebox.showinfo("Open Status",which.name+" has openned")
        else:
            messagebox.showinfo("Open Status","File is invalid")
        
    def saving(self):
        messagebox.showinfo("Save File","File Save process initiated")
        types=[
            ('All Files','*.*'),
            ('Java Files','*.java'),
            ('Python Files','*.py')
            ]
        hai=asksaveasfile(filetypes=types,defaultextension=types)
        
        hai.write(self.area.get(1.0,END))
        
        messagebox.showinfo("Save Status",hai.name+" file has saved")

ed=Editor()
ed.mainloop()
        
        