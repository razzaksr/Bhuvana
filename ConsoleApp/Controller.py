# Storages and operation's implementation

from Model import Corporate
from pickle import *

class CorporateDirectory:
    # permanant memory
    __file="D:\\Course backups\\Python\\Bhuvana\\cordirect.doc"
    # temporary memory
    __directory={}
    
    '''def __init__(self):
        hey=open(CorporateDirectory.__file,"wb")
        dump(CorporateDirectory.__directory,hey)
        print("Few basic corporates written in a file")'''
    
    def __mul__(self,other):
        
        # load from the file to temporary directory
        tmpFile=open(CorporateDirectory.__file,"rb")
        CorporateDirectory.__directory=load(tmpFile)
        tmpFile.close()
        
        key=other[0]
        obj=other[1]
        
        if key in CorporateDirectory.__directory:
            return str(CorporateDirectory.__directory[key])+" found "+key
        else:
            tmp=[]
            for k,v in CorporateDirectory.__directory.items():
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
        
        # load encrypted content from file to temporary memory directory
        CorporateDirectory.__directory=load(open(CorporateDirectory.__file,"rb"))
        
        hai=list(CorporateDirectory.__directory.items())
        hai.sort()
        CorporateDirectory.__directory=dict(hai)
        for k,v in CorporateDirectory.__directory.items():
            info+=str(k)+" - "+str(v)+"\n"
        return info
    
    def __add__(self,other):
        key,value=other[0],other[1]
        
        # load from the file to temporary directory
        tmpFile=open(CorporateDirectory.__file,"rb")
        CorporateDirectory.__directory=load(tmpFile)
        tmpFile.close()
        
        # after the loaded values from file add new item
        CorporateDirectory.__directory[key]=value
        
        # in order to insert an item permanantly dump temporary directory to file
        tmpFile=open(CorporateDirectory.__file,"wb")
        dump(CorporateDirectory.__directory,tmpFile)
        tmpFile.close()
        
        print(value.getOrg(),"has added in directory with",key)
    
    def __rshift__(self,key):
        # load from the file to temporary directory
        tmpFile=open(CorporateDirectory.__file,"rb")
        CorporateDirectory.__directory=load(tmpFile)
        tmpFile.close()
        if key in CorporateDirectory.__directory.keys():
            return CorporateDirectory.__directory[key]
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
        # loading from file 
        tmpFile=open(CorporateDirectory.__file,"rb")
        CorporateDirectory.__directory=load(tmpFile)
        tmpFile.close()
        
        if type(key) is str:
            if key in CorporateDirectory.__directory.keys():
                CorporateDirectory.__directory.pop(key)#del CorporateDirectory.__directory[key]
                # in order to impact in permanant storage dump to the file
                tmpFile=open(CorporateDirectory.__file,"wb")
                dump(CorporateDirectory.__directory,tmpFile)
                tmpFile.close()
                return "deletion done on "+key
        elif type(key) is Corporate:
            for eachk,eachv in CorporateDirectory.__directory.items():
                if key.getOrg() == eachv.getOrg() and eachv.getRatings()==key.getRatings():
                    CorporateDirectory.__directory.pop(eachk)
                    # in order to impact in permanant storage dump to the file
                    tmpFile=open(CorporateDirectory.__file,"wb")
                    dump(CorporateDirectory.__directory,tmpFile)
                    tmpFile.close()
                    return "deletion done on "+key.getOrg()
        else:
            return str(key)+" corporate doesn't exists"
    
    def __lshift__(self,other):
        
        # loading from file 
        tmpFile=open(CorporateDirectory.__file,"rb")
        CorporateDirectory.__directory=load(tmpFile)
        tmpFile.close()
        
        key=other[0]
        obj=other[1]
        #print(key,obj.getOrg())
        pair=[]
        if key!="" and key in CorporateDirectory.__directory.keys():
            #print("Key based update on",CorporateDirectory.__directory[key])
            pair.append(key)
            pair.append(CorporateDirectory.__directory[key])
        
        elif obj.getOrg()!="":
            for eachk,eachv in CorporateDirectory.__directory.items():
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
            CorporateDirectory.__directory[pair[0]]=pair[1]
            
            # in order to impact in permanant storage dump to the file
            tmpFile=open(CorporateDirectory.__file,"wb")
            dump(CorporateDirectory.__directory,tmpFile)
            tmpFile.close()
            
            print(pair[0],"has updated as\n",CorporateDirectory.__directory[pair[0]])
    

# dir1=CorporateDirectory()
# #print(dir1)

# while True:
#     print("\n1.add\n2.list\n3.edit\n4.delete\n5.read\n6.search");
#     choice=int(input("Enter the choice by number: "))
#     if choice == 1:
#         obj=dir1.getCorporate()
#         k=input("Tell us short form of this company: ")
#         dir1+[k,obj]
#     elif choice == 2:
#         print(dir1)
#     elif choice == 3:
#         based=input("Based on what you wish to update: key or org")
#         if based =="key":
#             print(dir1-input("Enter the org short form"))
#         elif based ==  "org":
#             obj=Corporate(org=input("Enter the company name"),rate=float(input("Tell us rating:")))
#             print(dir1-obj)
#         else:
#             print(based,"not match with anything")
#     elif choice == 4:
#         based=input("Based on what you wish to delete: key or org")
#         if based =="key":
#             print(dir1-[input("Enter the org short form"),object])
#         elif based ==  "org":
#             obj=Corporate(org=input("Enter the company name"))
#             dir1<<["",obj]
#         else:
#             print(based,"not match with anything")
#     elif choice == 5:
#         print(dir1>>input("Enter the org short form"))
#     elif choice ==6:
#         based=input("Based on what you wish to search: key, nature, opnnings,ratings")
#         if based == "nature":
#             print(dir1*["",Corporate(nature=input("Tell us nature: "))])
#         elif based == "ratings":
#             print(dir1*["",Corporate(rate=float(input("Tell us rating:")))])
#         elif based == "opennings":
#             print(dir1*["",Corporate(open=input("Enter the skill: "))])
#         elif based == "key":
#             print(dir1*[input("Enter the short form"),Corporate()])
#         else:
#             print(based,"not match with anything")
#     else:break
    


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
