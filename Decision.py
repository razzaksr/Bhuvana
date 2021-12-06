# Control statements:


# red bus

dest=input("Tell us where you wish to travel: ")

dest=dest.lower()

if dest=='chennai':
    print("multiple coaches available for",dest)
    timings=float(input("Tell us timing wish to travel: "))
    if timings>=00.01 and timings <=6.00:
        print("Early morning express")
        cash=int(input("Enter the amount: "))
        if cash>=250:
            print("Your Sleeper seat booked")
        elif cash>=140:
            print("Your Pushpack seater booked")
        else:
            print("Insufficient amount to book ticket")
    elif timings>=6.01 and timings <=12.00:
        print("Morning express")
        cash=int(input("Enter the amount: "))
        if cash>=350:
            print("Your Sleeper seat booked")
        elif cash>=190:
            print("Your Pushpack seater booked")
        else:
            print("Insufficient amount to book ticket")
    elif timings>=12.01 and timings <=18.00:
        print("Afternoon express")
        cash=int(input("Enter the amount: "))
        if cash>=500:
            print("Your Sleeper seat booked")
        elif cash>=250:
            print("Your Pushpack seater booked")
        else:
            print("Insufficient amount to book ticket")
    elif timings>=18.01 and timings <=23.59:
        print("Evening express")
        cash=int(input("Enter the amount: "))
        if cash>=600:
            print("Your Sleeper seat booked")
        elif cash>=300:
            print("Your Pushpack seater booked")
        else:
            print("Insufficient amount to book ticket")

elif dest=='bangalore':
    print("multiple coaches available for",dest)
    timings=float(input("Tell us timing wish to travel: "))
    if timings>=00.01 and timings <=6.00:
        print("Early morning express")
        cash=int(input("Enter the amount: "))
        if cash>=250:
            print("Your Sleeper seat booked")
        elif cash>=140:
            print("Your Pushpack seater booked")
        else:
            print("Insufficient amount to book ticket")
    elif timings>=6.01 and timings <=12.00:
        print("Morning express")
        cash=int(input("Enter the amount: "))
        if cash>=350:
            print("Your Sleeper seat booked")
        elif cash>=190:
            print("Your Pushpack seater booked")
        else:
            print("Insufficient amount to book ticket")
    else:
        print("Invalid timing")

else:
    print("There is no coaches available for",dest)