'''
$@ $$
@@ @$
.
.
.

'''

chart=""

for row in range(1,6):
    for seat in range(1,5):
        amt=int(input("Amount of ticket:"))
        if amt>=300:
            print("Ticket booked @",row,"th row",seat,"th seat")
            chart+="$"
        else:
            print("Insufficient amount to book ticket")
            chart+="@"
        if seat==2:
            chart+=" "
    chart+="\n"
else:
    print(chart)