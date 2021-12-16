# linear search

yet=[34.6,90.4,76.4,12.5,23.6,87.5,78.4,120.5,34.6,90.4,12.5]

hi=["vikas","varun","balaji","hemsworth","vanathi","holland","aarthi"]
hi.sort()
hi.reverse()
hello=tuple(hi)

def linear(data,index=0):
    if index<len(yet):
        if data==yet[index]:
            return index
        index+=1
        return linear(data,index)
    else:
        return -1

print(linear(78.4))
print(linear(0.00001))

def binary(data,start=0,end=len(hello)):
    if start<end:
        mid=(end+start)//2
        if hello[mid]==data:
            return mid
        elif data<hello[mid]:
            return binary(data,mid+1,end)
        else:
            return binary(data,start,mid)
    else:
        return -1

print(binary("vanathi"))
print(binary("holland"))
print(binary("evans"))