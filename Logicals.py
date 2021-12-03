# Logical Operation: and or not

'''
# cash withdrawl process

myAccount={
    "name":"Bhuvana",
    "number":11223456,
    "balance":980.45,
    "key":45
}

num=int(input("Account number please: "))
paskey=int(input("Encryption key: "))
paskey>>=2
amount=int(input("Tell us required cash: "))
print("Withdrawl status",(num == myAccount['number'] and paskey==myAccount['key']and amount<=myAccount["balance"]))'''


# loan Process

annual=float(input("Tell us annual income: "))
itr=int(input("Number of years ITR filed: "))
prop=int(input("Tell us Property value"))


print("Home Loan: ",(annual>=3.5 and itr>=2 or prop>=7))
print("Business Loan: ",(itr>=7 or prop>=10 and annual>=25))
print("Credit card limit of 1Lack: ",(not annual>=5))
