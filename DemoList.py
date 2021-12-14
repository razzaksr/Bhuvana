# List demonstration: temporary dynamic storage: Create Read Update Delete List search sort

'''
append, insert, remove, count, index,......
'''

hello=["vikas","varun","balaji","hemsworth","vanathi","holland","aarthi"]

#list
print(hello)
'''
for data in hello:print(data)

for pos in range(len(hello)):print(hello[pos])'''

# slicing: read
print(hello[5]) # read

print(hello[:]) # all

print(hello[2:]) # 3 to end

print(hello[:4]) # top 4

print(hello[::-1]) # reverse

# create
hello.append("Howard")
hello.insert(2,"raju")

print(hello)

# update
hello[3]="thamarai"

# deletion
hello.remove("varun")
del hello[3]
hello.pop()

print(hello)

print(hello.index("holland"))

hello.sort()
hello.reverse()

print(hello)

print(len(hello))
print(max(hello))
print(min(hello))

print(hello.count("aarthi"))