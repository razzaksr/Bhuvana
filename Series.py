# 1,3,5,7,9,11.........

limit=int(input("Set the limit: "))

'''
for num in range(1,limit+1,+2):
    print(num)
'''
# 2,4,6,8,10,12.........
'''for num in range(2,limit+1,+2):
    print(num)'''
    
# 2,3,5,7,11,13.........
'''
for num in range(2,limit+1):
    if num==2 or num==3 or num==5 or num==7 or num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
        print(num)
'''

# factorial: 54321=120
'''res=1
for limit in range(limit,0,-1):
    res*=limit
else:
    print(res)'''
    
# fibonacci: 0112358....

num1=0
num2=1

if limit==2:
    print(num1)
    print(num2)
elif limit>2:
    print(num1)
    print(num2)
    limit-=2
    for it in range(limit,0,-1):
        sum=num1+num2
        print(sum)
        num1=num2
        num2=sum
else:
    print("can't generate fibonacci")
        