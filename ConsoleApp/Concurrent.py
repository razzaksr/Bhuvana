from ExceptionClass import CorporateError
from Controller import *
from threading import *

class Access(Thread):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        hold.acquire()
        print("welcome",self.name,"to Corporate Buddy")
        
        dir1=CorporateDirectory()
        #print(dir1)
        while True:
            print("\n1.add\n2.list\n3.edit\n4.delete\n5.read\n6.search");
            try:
                choice=int(input("Enter the choice by number: "))
            except ValueError as ve:
                print(ve,"\nChoice always number")
                choice=int(input("Enter the choice by number: "))
            if choice == 1:
                obj=dir1.getCorporate()
                k=input("Tell us short form of this company: ")
                dir1+[k,obj]
            elif choice == 2:
                print(dir1)
            elif choice == 3:
                try:
                    based=input("Based on what you wish to update: key or org: ")
                    if based =="key":
                        dir1<<[input("Enter the org short form"),Corporate()]
                    elif based ==  "org":
                        obj=Corporate(org=input("Enter the company name"))
                        dir1<<["",obj]
                    else:
                        raise CorporateError()
                except CorporateError as ce:
                    print(ce,"\n",based,"not match with anything")
                    based=input("Based on what you wish to update: key or org: ")
                    if based =="key":
                        dir1<<[input("Enter the org short form"),object]
                    elif based ==  "org":
                        obj=Corporate(org=input("Enter the company name"))
                        dir1<<["",obj]
                    else:
                        print("Chances are over")
            elif choice == 4:
                based=input("Based on what you wish to delete: key or org")
                if based =="key":
                    print(dir1-input("Enter the org short form"))
                elif based ==  "org":
                    obj=Corporate(org=input("Enter the company name"),rate=float(input("Tell us rating:")))
                    print(dir1-obj)
                else:
                    print(based,"not match with anything")
            elif choice == 5:
                print(dir1>>input("Enter the org short form"))
            elif choice ==6:
                based=input("Based on what you wish to search: key, nature, opennings,ratings")
                if based == "nature":
                    print(dir1*["",Corporate(nature=input("Tell us nature: "))])
                elif based == "ratings":
                    print(dir1*["",Corporate(rate=float(input("Tell us rating:")))])
                elif based == "opennings":
                    print(dir1*["",Corporate(open=input("Enter the skill: "))])
                elif based == "key":
                    print(dir1*[input("Enter the short form"),Corporate()])
                else:
                    print(based,"not match with anything")
            else:
                print(self.name,"has done his/her work")
                break
        hold.release()

hold=Lock()

for numbers in range(1,5):
    thread=Access(input("Tell us username: "))
    thread.start()
    thread.join()
    

# t1=Access("Manoj")
# t2=Access("Vinayak")
# t3=Access("Prathap")
# t4=Access("Maran")

# t1.start()
# t2.start()
# t3.start()
# t4.start()

