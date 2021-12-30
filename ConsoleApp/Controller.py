# Storages and operation's implementation

from Model import Corporate

class CorporateDirectory:
    __directory={}
    def __init__(self):
        self.__directory={
            "cts":Corporate("Cognizant","Application","Python,Java","Chennai,Banglore",23000,2.8,4.1),
            "tcs":Corporate("Tata Consultancy Services","Application","Java,Javascript","Chennai,Banglore,Coimbatore",42000,2.1,4.3),
            "infy":Corporate("Infosys","Application","Python","Banglore",12000,1.5,3.5),
            "ibm":Corporate("IBM","Product","C,Java,C++","Chennai,Hyderabad,Cochin",7000,4.9,3.9),
            "zoho":Corporate("ZOHO","Product","Python,Java,C","Chennai",11000,3.9,4.8),
        }
    
    def __mul__(self,other):
        key=other[0]
        obj=other[1]
        
        if key in self.__directory:
            return str(self.__directory[key])+" found "+key
        else:
            tmp=[]
            for k,v in self.__directory.items():
                if obj.getNature()!="" and obj.getOpnnings()=="" and  obj.getRatings()==0.0:
                    if v.getNature()==obj.getNature():
                        tmp.append(k+" "+str(v.getOrg()))
                elif obj.getNature()=="" and obj.getOpnnings()!="" and obj.getRatings()==0.0:
                    if obj.getOpnnings() in v.getOpnnings():
                        tmp.append(k+" "+str(v.getOrg()))
                elif obj.getNature()=="" and obj.getOpnnings()=="" and obj.getRatings()!=0.0:
                    if v.getRatings()>=obj.getRatings():
                        tmp.append(k+" "+str(v.getOrg()))
            else:
                if len(tmp)>0:return str(tmp)
                else:return str(obj)+" not match"
                
    def __str__(self):
        info = "Directory had following corporates\n"
        hai=list(self.__directory.items())
        print("Before Sort:\n",hai)
        hai.sort()
        print(str(hai))
        self.__directory=dict(hai)
        for k,v in self.__directory.items():
            info+=str(k)+" - "+str(v)+"\n"
        return info
    
    def __add__(self,other):
        key,value=other[0],other[1]
        self.__directory[key]=value
        print(value.getOrg(),"has added in directory with",key)
    
    def __rshift__(self,key):
        if key in self.__directory.keys():
            return self.__directory[key]
        else:
            return key+" doesn't match with any corporate"
    
    def getCorporate(self):
        obj=Corporate()
        obj.setOrg(input("Tell us corporate name: "))
        obj.setEmployees(int(input("Tell us no of employees: ")))
        obj.setMinSal(float(input("Tell us basic salary of this company: ")))
        obj.setNature(input("Tell us nature of industry: "))
        obj.setOpennings(input("Tell us technology where it has opnnings: "))
        obj.setPlace(input("Tell us campus locations: "))
        obj.setRatings(float(input("Tell us rating for this companay: ")))
        return obj
    
    def __sub__(self,key):
        if type(key) is str:
            if key in self.__directory.keys():
                self.__directory.pop(key)#del self.__directory[key]
                return "deletion done on "+key
        elif type(key) is Corporate:
            for eachk,eachv in self.__directory.items():
                if key.getOrg() == eachv.getOrg() and eachv.getRatings()==key.getRatings():
                    self.__directory.pop(eachk)
                    return "deletion done on "+key.getOrg()
        else:
            return str(key)+" corporate doesn't exists"
    
    def __lshift__(self,other):
        key=other[0]
        obj=other[1]
        #print(key,obj.getOrg())
        pair=[]
        if key!="" and key in self.__directory.keys():
            #print("Key based update on",self.__directory[key])
            pair.append(key)
            pair.append(self.__directory[key])
        
        elif obj.getOrg()!="":
            for eachk,eachv in self.__directory.items():
                if eachv.getOrg()==obj.getOrg():
                    pair.append(eachk)
                    pair.append(eachv)
        
        if len(pair)!=0:
            #print(pair[0],pair[1])
            prop=input("Tell us property of Corporate "+pair[0]+": ")
            if prop == "org":
                pair[1].setOrg(input("Tell us new org name: "))
            elif prop=="nature":
                pair[1].setNature(input("Tell us new nature of "+ pair[1].getOrg() +" : "))
            elif prop=="opnnings":
                pair[1].setOpennings(input("Tell us new opnnings skill of "+ pair[1].getOrg() +" : "))
            elif prop=="place":
                pair[1].setPlace(input("Tell us places of "+ pair[1].getOrg() +" : "))
            elif prop=="employees":
                pair[1].setEmployees(int(input("Tell us no of employees of "+ pair[1].getOrg() +" : ")))
            elif prop=="salary":
                pair[1].setMinSal(float(input("Tell us minium salary of "+ pair[1].getOrg() +" : ")))
            elif prop=="rate":
                pair[1].setRatings(float(input("Tell us current ratings of "+ pair[1].getOrg() +" : ")))
            else:
                print(prop,"not match any of Corporate attribute")
            self.__directory[pair[0]]=pair[1]
            print(pair[0],"has updated as\n",self.__directory[pair[0]])
    

dir1=CorporateDirectory()
#print(dir1)

while True:
    print("\n1.add\n2.list\n3.edit\n4.delete\n5.read\n6.search");
    choice=int(input("Enter the choice by number: "))
    if choice == 1:
        obj=dir1.getCorporate()
        k=input("Tell us short form of this company: ")
        dir1+[k,obj]
    elif choice == 2:
        print(dir1)
    elif choice == 3:
        based=input("Based on what you wish to update: key or org")
        if based =="key":
            print(dir1-input("Enter the org short form"))
        elif based ==  "org":
            obj=Corporate(org=input("Enter the company name"),rate=float(input("Tell us rating:")))
            print(dir1-obj)
        else:
            print(based,"not match with anything")
    elif choice == 4:
        based=input("Based on what you wish to delete: key or org")
        if based =="key":
            print(dir1-[input("Enter the org short form"),object])
        elif based ==  "org":
            obj=Corporate(org=input("Enter the company name"))
            dir1<<["",obj]
        else:
            print(based,"not match with anything")
    elif choice == 5:
        print(dir1>>input("Enter the org short form"))
    elif choice ==6:
        based=input("Based on what you wish to search: key, nature, opnnings,ratings")
        if based == "nature":
            print(dir1*["",Corporate(nature=input("Tell us nature: "))])
        elif based == "ratings":
            print(dir1*["",Corporate(rate=float(input("Tell us rating:")))])
        elif based == "opennings":
            print(dir1*["",Corporate(open=input("Enter the skill: "))])
        elif based == "key":
            print(dir1*[input("Enter the short form"),Corporate()])
        else:
            print(based,"not match with anything")
    else:break
    


'''# search: key, rating, nature, opennings
print(dir1*["",Corporate(nature="Application")])
print(dir1*["",Corporate(rate=3.8)])
print(dir1*["",Corporate(open="Java")])
print(dir1*["infy",Corporate()])
'''

'''
# update
obj=Corporate("Cognizant","Application","Python,Java","Chennai,Banglore",23000,2.8,4.1)
dir1<<["tcs",object]
dir1<<["",obj]

print(dir1)
'''

'''
# deletion
obj=Corporate("Infosys","Application","Python","Banglore",12000,1.5,3.5)
print(dir1-"tcs")
print(dir1-obj)
'''

# collect required data to create new corporate
'''obj=Corporate(
    input("Tell us corporate name: "),
    input("Tell us nature of industry: "),
    input("Tell us technology where it has opnnings: "),
    input("Tell us campus locations: "),
    int(input("Tell us no of employees: ")),
    float(input("Tell us basic salary of this company: ")),
    float(input("Tell us rating for this companay: "))
)'''
'''
obj=dir1.getCorporate()
k=input("Tell us short form of this company: ")

dir1+[k,obj]

print(dir1)
'''

'''# read
print(dir1>>"tcs")
print(dir1>>"infv")
'''
