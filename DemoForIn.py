cast=["Chris Evans","Scarlet Jhonson","Robert Downey","Chris Hemsworth","Tom Holland","Chris Pratt","Tom Hiddlson"]

for content in cast:
    if content.startswith("Ch"):
        print(content)
        
myData={"Name":"Razak Mohamed S",5000:["java","python"],10000:["spring","hibernate","node"],
        "Javascript":"React","Java":"RestAPI","Python":"DJango",
        "C#":"ASP"}

for key in myData.keys():
    if type(key) == str:
        if myData[key].startswith("Re"):
            print(key,myData[key])