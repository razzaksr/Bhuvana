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
    
    def __str__(self):
        info = "Directory had following corporates\n"
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
obj=Corporate("Cognizant","Application","Python,Java","Chennai,Banglore",23000,2.8,4.1)
# update
dir1<<["tcs",object]
dir1<<["",obj]

print(dir1)


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
