'''
Single task multithread:

'''

from threading import *

class Machine(Thread):
    __tickets=50
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        print("welcome",self.name,"to INOX")
        count=int(input("Tell us how many tickets you want: "))
        if count<=Machine.__tickets:
            amt=int(input("Enter the amount for "+str(count)+" : "))
            if amt>=(count*210):
                Machine.__tickets-=count
                print(count,"tickets are provided to",self.name)
            else:
                print(self.name,"hasn't booked the tickets due to insufficient amount")
        else:
            print(count,"tickets couldn't booked by",self.name,"due to availablility")

m1=Machine("Sarathy")
m2=Machine("Manoj")
m3=Machine("Sabari")
m4=Machine("Vijay")
m1.start()
m1.join() # one by one synchronization
m2.start()
m2.join()
m3.start()
m3.join()
m4.start()