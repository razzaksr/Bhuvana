from Inheritance import Google

class Bank:
    def __init__(self,accno=0,bal=0.0):
        self.accno=accno
        self.accbal=bal
    def __str__(self):
        return str(self.accno)+" "+str(self.accbal)+"\n"
        
class GPay(Google,Bank):# multiple, hybrid
    upiPin=0
    plans={
        "jio":[1200,450,213,299,599,399],
        "airtel":[988,322,199,99,299,1099,349],
        "bsnl":[75,32,21,90,365,199,320,900]
    }
    def __init__(self, user="", email="", con=0, upi=0, an=0,ab=0.0):
        self.username=user
        self.email=email
        self.contact=con
        self.upiPin=upi
        self.accno=an
        self.accbal=ab
    
    def __lshift__(self,one):
        user=int(input("Enter the UPI PIN to validate: "))
        if user==self.upiPin:
            if one[1]<=self.accbal:
                self.accbal-=one[1]
                print(one[1],"will be transferred to",one[0],"by",self.username)
            else:
                print(self.username,"couldn't send the amount due to insufficient balance")
        else:
            print(self.username,"has entered wrong UPI PIN")
    
    def __rshift__(self,one):
        user=int(input("Enter the UPI PIN to validate: "))
        if user==self.upiPin:
            if one[2] in self.plans.keys():
                if one[1] in self.plans[one[2]]:
                    if one[1]<=self.accbal:
                        print(one[0],"number will be recharged with",one[1],"of",one[2],"network by",self.username)
                    else:
                        print(self.username,"couldn't recharge due to insufficient balance")
                else:
                    print("Unkown plan",one[1],"in",one[2],"network")
            else:
                print(one[2],"network not approved by GPay")
        else:
            print(self.username,"has entered wrong UPI PIN")
g1=GPay("rasheedha","rasheedha@gmail.com",9876567987,112233,987656788,2348.9)

print(g1)

g1<<['mohamed@okaxis',920]
g1>>[9876543210,427.8,'jio']

g1>>[8765566544,99,'airtel']
g1>>[8765566544,99,'vi']
g1<<['sabari@okicici',4000]
