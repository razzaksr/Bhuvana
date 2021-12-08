# Loop control keywords: continue break

# bus reservation:

'''seats=30

while seats>0:
    if seats%2==0:
        print("Already booked @ ",seats)
        seats-=1
        continue
    else:
        count=int(input("No of seats required: "))
        if count<=seats:
            calculated=count*290
            amt=int(input("Enter the amount: "))
            if amt>=calculated:
                print("Seat's",count,"Booked")
                seats-=count
            else:
                print("Insufficient amount")
        else:
            print("Lack of seats")'''
            
seats=30

while seats>0:
    if seats%2==0:
        print("Already booked @ ",seats)
        seats-=1
        #continue
        break
    else:
        amt=int(input("Enter the amount: "))
        if amt>=290:
            print("Seat's",seats,"Booked")
            seats-=1
        else:
            print("Insufficient amount")