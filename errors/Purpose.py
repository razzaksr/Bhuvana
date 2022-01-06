alpha=0
beta=0
try:
    alpha=int(input("Enter the number1: "))
    beta=int(input("Enter the number2: "))

    #alpha,beta=beta,alpha

    alpha*=beta
    beta=alpha//beta
    alpha//=beta

except ValueError as ve:
    print(ve,"\nEnter the whole numbers")
    alpha=int(input("Enter the number1: "))
    beta=int(input("Enter the number2: "))
    alpha*=beta
    beta=alpha//beta
    alpha//=beta
finally:
    print(alpha,beta)