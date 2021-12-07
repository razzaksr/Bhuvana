# looping statements

myAssets=["Avenger220",45000,"Ignis",20,"House",89.3]

print(myAssets)

# for in iteration:

for ptr in myAssets:
    print(ptr)

# for in range iteration
    
for pos in range(0,len(myAssets)):
    print(pos,myAssets[pos])
    
for pos in range(len(myAssets)-1,-1,-1):
    print(pos,myAssets[pos])


# while iteration
pos=0
while pos<len(myAssets):
    print(myAssets[pos])
    data=int(input("Next steps: "))
    pos+=data

