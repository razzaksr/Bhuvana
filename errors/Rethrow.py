# single try multi except
from array import *

each=array('i',[12,56,85,56,467,245,876,2,45,6])

pos,val=0,0

def update():
    try:
        pos=int(input("tell us index to update: "))
        val=int(input("Tell us value to update: "))
        each[pos]=val;
        print(each[pos]," has updated")
    except IndexError as ie:
        print(ie,"inside an update function")
        raise ie
    except ValueError as ve:
        print(ve,"inside an update function")
        raise ve
    except TypeError as Tp:
        print(Tp,"inside an update function")
        raise Tp


try:
    update()
except IndexError as ie:
    print(ie,"\nIndex within",len(each))
    pos=int(input("tell us index to update: "))
    val=int(input("Tell us value to update: "))
    each[pos]=val;
    print(each[pos]," has updated")
except ValueError as ve:
    print(ve,"value should be numeric")
    pos=int(input("tell us index to update: "))
    val=int(input("Tell us value to update: "))
    each[pos]=val;
    print(each[pos]," has updated")
except TypeError as Tp:
    print(Tp)
    got=val+(val*0.123);
    print("What actual result: ",got)
    each[pos]=int(got);
    print(each[pos]," has updated")