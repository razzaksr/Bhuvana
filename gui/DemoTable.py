# table: combination entry

from tkinter import *


class MyTable(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Table Demo")
        self.geometry('500x300')
        
        self.h1=Entry(self)
        self.h1.insert(END,"Organisation Name")
        self.h1.grid(row=0,column=0)
        
        self.h2=Entry(self)
        self.h2.insert(END,"Organisation Type")
        self.h2.grid(row=0,column=1)
        
        self.h3=Entry(self)
        self.h3.insert(END,"Organisation Location")
        self.h3.grid(row=0,column=2)
        
        self.h4=Entry(self)
        self.h4.insert(END,"Organisation Apps")
        self.h4.grid(row=0,column=3)
        
        self.datarow1=Entry(self)
        self.datarow1.insert(END,"Wipro")
        self.datarow1.grid(row=1,column=0)
        
        self.datarow2=Entry(self)
        self.datarow2.insert(END,"Service Sector")
        self.datarow2.grid(row=1,column=1)
        
        self.datarow3=Entry(self)
        self.datarow3.insert(END,"Mysore")
        self.datarow3.grid(row=1,column=2)
        
        self.datarow4=Entry(self)
        self.datarow4.insert(END,"Passport Seva")
        self.datarow4.grid(row=1,column=3)
        
        self.mydict={
            "name":["Cognizant","TCS","Accenture","Infosys"],
            "type":["Product Sector","Service Sector","BPO","Service Sector"],
            "location":["Banglore","Chennai","Covai","Chennai"],
            "apps":["incometaxindia","icici","irctc","axisbank"]
        }
        
        line=2
        for x in self.mydict.keys():
            col=0
            for v in self.mydict[x]:
                self.tmpbox=Entry(self)
                self.tmpbox.insert(END,v)
                self.tmpbox.grid(row=line,column=col)
                col+=1
            line+=1
            

my=MyTable()
my.mainloop()
