from threading import *

import time

class Machine(Thread):
    __tickets=50
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        print("welcome",self.name,"to INOX")
        hold.acquire();
        count=int(input("Tell us how many tickets "+self.name+" want: "))
        if count<=Machine.__tickets:
            amt=int(input("Enter the amount for "+str(count)+" : "))
            payable=count*210;
            if amt>=payable:
                Machine.__tickets-=count
                if amt-payable>0:
                    time.sleep(10)
                    print("balance",(amt-payable),"has returned")
                print(count,"tickets are provided to",self.name)
            else:
                print(self.name,"hasn't booked the tickets due to insufficient amount")
        else:
            print(count,"tickets couldn't booked by",self.name,"due to availablility")
        hold.release()
        print("thanks for having",self.name,"in our INOX")


hold=Lock()

m1=Machine("Sarathy")
m2=Machine("Manoj")
m3=Machine("Sabari")
m4=Machine("Vijay")
m1.start()
m2.start()
m3.start()
m4.start()