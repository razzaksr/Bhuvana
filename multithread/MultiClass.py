'''
Multi task multithread: using Thread
'''

from threading import *

class Mall:
    # Mall has contains two classes Games and Shopping
    
    class Shopping(Thread):
        Stock=3
        def __init__(self, name=""):
            super().__init__()
            self.name=name
        def run(self):
            amt=int(input(self.name+"Enter the amount: "))
            if amt>=23000:
                print(self.name,"bought the AC")
                Mall.Shopping.Stock-=1
            else:
                print("Insufficient to buy by",self.name)
    class Games(Thread):
        def __init__(self, name=""):
            super().__init__()
            self.name=name
        
        def run(self):
            print(self.name,"intrested to play Snow games")
            age=int(input(self.name+" Enter the age: "))
            if age>=18 and age<=51:
                print(self.name,"Enjoy playing snow games")
            else:
                print(self.name,"not allowed in this primises")



s1=Mall.Shopping("Sheik")
g1=Mall.Games("Razak")
s2=Mall.Shopping("Sabari")
g2=Mall.Games("Mohamed")

s1.start()
g1.start()

s2.start()
g2.start()