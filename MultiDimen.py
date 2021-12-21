# apartment

apart=[[9100,3400,5100,12900],[4100,5600,4200],[1900,12000],[4500,6000,3100,2500,9000,10500]]

def assign(data,floor=0,house=0):
    #floor=int(input("Tell us floor: "))
    #house=int(input("Tell us house number: "))
    apart[floor][house]=data
    print(data,"assigned @",floor,"th floor",house,"th house")

def visit():
    print("Available tenants with their rents")
    for floor in range(len(apart)):
        #for house in range(len(apart[floor])):print(apart[floor][house])
        for house in apart[floor]:print(house,end=" ")
        print()

def read(f,h):
    return apart[f][h]

def erase(f,h):
    del apart[f][h]
    #apart[f].remove(h)
    print("house",h,"in",f,"floor has no longer for tenants")

def search(budget):
    print("Available house with budget of",budget)
    for floor in range(len(apart)):
        for house in range(len(apart[floor])):
            if apart[floor][house]<=budget:
                print(floor,"th floor",house,"th house for",apart[floor][house])
                
def order():
    for floor in range(len(apart)):
        for select in range(len(apart[floor])):
            for com in range(select+1,len(apart[floor])):
                if apart[floor][select]<apart[floor][com]:
                    #swap
                    apart[floor][select],apart[floor][com]=apart[floor][com],apart[floor][select]
                    '''apart[floor][select]^=apart[floor][com]
                    apart[floor][com]^=apart[floor][select]
                    apart[floor][select]^=apart[floor][com]'''

def binary(data,floor=0,start=0,end=len(apart[0])-1):
    print("Searchin @ ", floor, "between ",start," and ",end)
    if start<end and floor<len(apart):
        mid=(end+start)//2
        if apart[floor][mid] == data: 
            return [str(floor)+"th floor",str(mid)+"th house"]
        elif data < apart[floor][mid]:
            return binary(data,floor,mid+1,end)
        else:
            return binary(data,floor,start,mid)
    elif floor<len(apart):
        floor+=1
        return binary(data,floor,0,len(apart[floor])-1)
    else:
        return -1