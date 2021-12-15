# Demo dictionary: {key:value}: CRUDL

skillset={"web":["java","javascript"],
          "mobile":["android"],
          "desktop":["java"]}

# list
print(skillset)

for x in skillset.items():
    print(x)

for k,v in skillset.items():
    print(k,v)

for key in skillset.keys():
    print(key)

for value in skillset.values():
    print(value)
    

# read
print(skillset["web"])

# update
skillset["web"].append("PHP")
skillset["mobile"][0]="Swift"

#delete
skillset.pop("web")
skillset.popitem()

# create
skillset["testing"]=["JUnit","Mockito","Selenium"]

print(skillset)