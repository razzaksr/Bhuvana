# Arithmetic Operator:
'''
# milage calculator
fuel=int(input("Tell us no of liters filled: "))
kms=int(input("Tell us no of kms has driven: "))

milage=kms//fuel

#print("Milage is",milage)
print("Milage is \n%d"%(milage))

ml=fuel/kms

#print("Fuel consumed per km",ml)

print("Fuel\t consumed per km\r%.3f" % (ml))
'''

'''
# Tax deduction

ctc=float(input("Tell us annual income: "))
tax=float(input("Tell us tax: "))

ctc=ctc-(ctc*tax)/100

print("Take Home is",ctc)
'''


marshmallow=6.3
lollipop=5.4
print(marshmallow)
print(lollipop)

'''# swap using + - >> numbers

marshmallow=marshmallow+lollipop
lollipop=marshmallow-lollipop
marshmallow=marshmallow-lollipop
'''

# swap using * / >> numbers

marshmallow=marshmallow*lollipop
lollipop=marshmallow/lollipop
marshmallow=marshmallow/lollipop

print(marshmallow,end=" ")
print(lollipop)


