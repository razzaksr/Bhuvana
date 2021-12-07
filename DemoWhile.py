# while loop


'''realme=56
order=0

while realme>0: # whether sale to be continued or not
    count=int(input("Tell us count of mobile you wish: "))
    if count<=realme:
        realme-=count
        print("Order of",count,"mobile's placed")
        order+=1
    else:
        print("available is",realme)

else:
    print("Out of stock")

print("Total orders of 56 mobiles",order)'''


realme=56
order=0
timeing=11.31

while realme>0 and timeing<=11.45: # whether sale to be continued or not
    count=int(input("Tell us count of mobile you wish: "))
    if count<=realme:
        realme-=count
        print("Order of",count,"mobile's placed")
        order+=1
    else:
        print("available is",realme)
    timeing+=0.01

else:
    print("Out of stock")

print("Total orders of 56 mobiles",order)