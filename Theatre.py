# no of shows and no of tickets booked


for shows in range(1,5):
    print("Show number",shows)
    available=30
    while available>0:
        count=int(input("No of tickets:"))
        if count<=available:
            calculated=count*230
            amt=int(input("Enter the amount: "))
            if amt>=calculated:
                print(count,"Tickets booked @",shows)
                available-=count
            else:
                print(count,"Tickets can't book due to insufficient amount")
        else:
            print("Only",available,"Available")
    else:
        print(shows,"Show tickets booking closed")
else:
    print("Show for the day over")