# Set: temporary dynamic storage without duplicates: CDL

yet={34.6,90.4,76.4,12.5,23.6,87.5,78.4,120.5,34.6,90.4,12.5}

# list
print(yet)

for data in yet:print(data)

#for data in range(len(yet)):print(yet[data])

# slice: read
#print(yet[9])

# create
yet.add(98.3)
#yet.add(8,98.3)
#yet.insert(2,76.00)

yet.remove(87.5)
yet.pop()

print(yet)