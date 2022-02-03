from pymysql import *
from tkinter import *

class Edit(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Edit Corporate")
        self.geometry("500x300")
        
        