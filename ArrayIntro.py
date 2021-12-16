from array import *

each=array('i',[12,45])

#list
print(each)
for data in each:print(data)

#create
#each.append("Razak")
each.append(90)
each.append(45)
each.append(88)
each.append(12)
each.append(76)

# read
print(each[:])
print(each[::-1])
print(each[2])

# update
each=each[::-1]
each[3]=77

print(each.count(12))

# delete
each.pop()
del each[2]
each.remove(45)

#print(each.index(45))

print(each)
print(len(each),max(each),min(each))

hai=[12,56,85,56,467,245,876,2,45,6]

each.fromlist(hai)

print(each)

hey=list(each)

hey.sort()

yet=array('i',[])

yet.fromlist(hey)

print(yet)