# Bitwise Operator: & | ^ >> <<

'''
1024 512 256 128 64 32 16 8 4 2 1
   0   0   0   0  0  1  0 0 0 0 0 >> 32
   0   0   0   0  0  0  0 1 1 0 1 >> 13
   
   0   0   0   0  0  1  0 1 1 0 1 >> 45>> myTank
   
   0   0   0   0  0  1  0 0 0 0 0 >> 32>> myBikeTank
   
   0   0   0   1  0  0  0 0 0 0 0 >> 128> 
   
   0   0   0   0  0  0  0 1 1 0 1 >> 13>> myTank
   
   0   0   0   0  0  0  0 0 0 0 1 >> 1
   
   0   1   0   0  0  0  0 1 0 0 0 >> 520
   
   0   1   0   0  0  1  0 1 0 0 0 >> 552
   
   
   1   0   0   1  1  0  1 0 0 1 0 >> 1234
   
   1   0   0   1  1  0  1 1 1 1 1 >> 1247
   
   0   0   0   0  0  0  0 0 0 0 0 >>  0
   
   
'''

myTank=32
myBikeTank=13

print(myTank & myBikeTank)
print(myBikeTank | 1234)

print(myTank ^ 520)



# swap by ^ 

myTank=myTank^myBikeTank
myBikeTank=myTank^myBikeTank
myTank=myTank^myBikeTank

print(myTank,myBikeTank)

print(myTank>>3)

print(myBikeTank<<2)
