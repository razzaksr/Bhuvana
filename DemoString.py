# String class:

org="zealous"

print(org)

print(org[0:4])

#update
org+" Tech Corp" # immutable

print(org)

org=org.upper()

print(org)

hello="vikas,varun,balaji,hemsworth,vanathi,holland,aarthi"

print(hello)

tmp=hello.split(",")

print(tmp)

print(tmp.index("balaji"))

print(tmp.count("vanathi"))


for x in tmp:
    if x.startswith("h",2,5):
        print(x)
    if x.endswith("i",3,len(x)):
        print(x)
    print(x.isalpha())
    print(x.isdigit())
    print(x.isalnum())

check="     zealous     "
print(len(check))
check=check.lstrip(" ")
print(len(check))
check=check.rstrip(" ")
print(len(check))

print(check*10)
print(check+" tech corp")

print(check.replace("eal","ael"))