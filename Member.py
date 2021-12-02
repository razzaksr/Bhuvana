# member Operator: in, not in

myFrame={"Spring","Hibernate","JPA","RestAPI","Flask","MySQL","RestAPI"}
myVendors=["TCS","Wipro","DLithe","Cognizant","L&T","Infogynix","TCS"]
myLanguages=("Java","Python","C","C#","Javascript")

myProfile={"lang":myLanguages,"work":myFrame,"exp":myVendors,"Name":"Razak Mohamed S"}

print(type(myFrame))
print(len(myFrame))
print(len(myVendors))

print('TCS' in myFrame)
print('C#' in myLanguages)
print('Spring' not in myLanguages)

print('PHP' in  myProfile['lang'])
print('Java' in myProfile['lang'][1])

print("zak" in myProfile["Name"])

print('&' in myVendors[4])