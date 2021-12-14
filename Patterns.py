'''
Patterns:
@@@@@
@@@@@
@@@@@
@@@@@
@@@@@
'''

count=int(input("Tell us count: "))

for row in range(1,count+1):
    for col in range(1,count+1):
        print("@",end="")
    print()
    
# left upper floyd
for row in range(1,count+1):
    for col in range(1,row+1):
        print("@",end="")
    print()

#left lower floyd
for row in range(count,0,-1):
    for col in range(1,row+1):
        print("@",end="")
    print()

# right upper floyd
for row in range(1,count+1):
    for space in range(count-1,row-1,-1):
        print("",end=" ")
    for col in range(1,row+1):
        print("@",end="")
    print()

# right lower floyd
for row in range(count,0,-1):
    for space in range(count-1,row-1,-1):
        print("",end=" ")
    for col in range(1,row+1):
        print("@",end="")
    print()

# pascal upper
for row in range(1,count+1):
    for space in range(count-1,row-1,-1):
        print("",end=" ")
    for col in range(1,row+1):
        print("@ ",end="")
    print()

# pascal lower
for row in range(count,0,-1):
    for space in range(count-1,row-1,-1):
        print("",end=" ")
    for col in range(1,row+1):
        print("@ ",end="")
    print()


limit=1

# pyramid upper
for row in range(1,count+1):
    for space in range(count-1,row-1,-1):
        print("",end=" ")
    for col in range(1,limit+1):
        print("@",end="")
    print()
    limit+=2


limit=(count*2)-1

# pyramid lower
for row in range(count,0,-1):
    for space in range(count-1,row-1,-1):
        print("",end=" ")
    for col in range(1,limit+1):
        print("@",end="")
    print()
    limit-=2
    
# time machine
limit=count+2
mid=(count//2)+1
for row in range(1,count+1):
    if row <= mid:
        for space in range(1,row):
            print("",end=" ")
        limit-=2
    else:
        limit+=2
        for space in range(count-1,row-1,-1):
            print("",end=" ")
    for col in range(1,limit+1):
        print("@",end="")
    print()