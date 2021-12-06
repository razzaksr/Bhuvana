# decision making

# tax deduction

ctc=float(input("Annual salary: "))

tax=0.0

if ctc>=5.1 and ctc<7.2:
    tax=2.5

elif ctc>=7.2 and ctc<10.5:
    tax=10.2

elif ctc>=10.5 and ctc<20.5:
    tax=15.9

elif ctc>=20.5 and ctc<30:
    tax=20.5
    
elif ctc>=30.1:
    tax=30.5

else:
    print("There is no deduction in your salary")

print(tax," tax will be deducted in your ",ctc)
takeHome=ctc-(ctc*tax)/100

print("Your take home is",takeHome)