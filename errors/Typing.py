# type error
from array import *

hi = "Ra7ak"
yet=array('i',[])
i=0
try:
    #i=chr(hi[2])
    yet.append('e')
    print("try bloack")
except TypeError as te:
    print(te,"\nType can't cast")
    #i=int(hi[2])
    yet.append(int(input("Tell us whole number:")))
finally:
    #print(i)
    print(yet)