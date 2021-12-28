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
    

dir1=CorporateDirectory()
#print(dir1)

'''
# deletion
obj=Corporate("Infosys","Application","Python","Banglore",12000,1.5,3.5)
print(dir1-"tcs")
print(dir1-obj)
'''
'''
# collect required data to create new corporate
obj=Corporate(
    input("Tell us corporate name: "),
    input("Tell us nature of industry: "),
    input("Tell us technology where it has opnnings: "),
    input("Tell us campus locations: "),
    int(input("Tell us no of employees: ")),
    float(input("Tell us basic salary of this company: ")),
    float(input("Tell us rating for this companay: "))
)
k=input("Tell us short form of this company: ")

dir1+[k,obj]

print(dir1)
'''

'''# read
print(dir1>>"tcs")
print(dir1>>"infv")
'''
