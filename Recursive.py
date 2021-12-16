# recursive function

'''hello=[[89,22,56,11],[89,12,56,87],[90,8,1,45],[87,43,31,26]]

print(hello[0][0])'''

def hai(times=1):
    if times<=10:
        print("Hai called",times)
        times+=1
        hai(times)
    else:
        return

def factorial(num,fact=1):
    if num>0:
        fact*=num
        num-=1
        return factorial(num,fact)
    else:
        return fact

from array import *

hi=array('i',[2500])

def state(count=1,deb=0):
    if count<10:
        amt=int(input("Current balance: "))
        hi.append(amt)
        if hi[count]<hi[count-1]:
            deb+=1
        count+=1
        state(count,deb)
    else:
        print(hi)
        deb-=3
        if deb>0:
            charges=(deb*20)
            hi.append(hi[len(hi)-1]-charges)
            print("Debit charges",charges,"will deducted from account")
        print("available balance:",hi[len(hi)-1])
        return

hai()
print(factorial(5))
print(factorial(7))
print(factorial(3))
print(factorial(2))

state()