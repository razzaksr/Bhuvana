# tuple : Temporary static storage: RL

hai=(87,34,90,11,45,76,34,12,20,87,55,54,87)

# list
print(hai)

#for h in hai:print(h)

#for pos in range(len(hai)):print(hai[pos])

# read: slicing
print(hai[:])
print(hai[2:6])
print(hai[::-1])

# create
#hai.append(120)
#hai.insert(0,120)

#update
#hai[0]=560

print(hai.count(87))
print(hai.index(20))