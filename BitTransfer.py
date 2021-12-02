# Using shift performing data transfer

print("**********Sender End**************")

data=int(input("Tell us data wish to transfer: "))
key=int(input("Tell threshold key: "))

senderData=data<<key

print("***************Receiver End***********")
print("Received data: ",senderData)
myKey=int(input("Tell us decrypt key: "))

receiverData=senderData>>myKey

print(data == receiverData)