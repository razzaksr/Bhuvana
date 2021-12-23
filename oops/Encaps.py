'''

Core of the application which runs on the class

'''

class Corporate:
    __org,__nature,__opennings,__place,__employees,__minSal,__ratings="","","","",0,0.0,0.0
    
    def __init__(self,org="",nature="",open="",plc="",emp=0,sal=0.0,rate=0.0):
        self.__org=org;self.__nature=nature;self.__opennings=open;self.__place=plc;self.__employees=emp
        self.__minSal=sal;self.__ratings=rate
    
    def __str__(self):
        return "Corporate name "+self.__org+" is "+self.__nature+" company has "+str(self.__ratings)+" in "+self.__place+" has resources of "+str(self.__employees)+" has offering jobs on "+self.__opennings+" with basic pay of "+str(self.__minSal)+"\n";
    
    def __add__(self,other):
        self.__ratings+=other
    
    def __gt__(self,other):
        if self.__ratings>=other.__ratings:
            return self.__org+" is best"
            #return str(self)
        else:
            return other.__org+" is best"
            #return str(other)
    
    def __eq__(self,other):
        for each in other:
            each=each.capitalize()
            if each in self.__opennings:
                print("Openning for",each,"available in",self.__org)
                return
        else:
            print(other,"skills are not matching in",self.__org)
    
        
        
    
    def setOrg(self,org):self.__org=org
    def getOrg(self):return self.__org
    def setNature(self,nature):self.__nature=nature
    def getNature(self):return self.__nature
    def setOpennings(self,open):self.__opennings=open
    def getOpnnings(self):return self.__opennings
    def setPlace(self,plc):self.__place=plc
    def getPlace(self):return self.__place
    def setEmployees(self,emp):self.__employees=emp
    def getEmployees(self):return self.__employees
    def setMinSal(self,sal):self.__minSal=sal
    def getMinSal(self):return self.__minSal
    def setRatings(self,rate):self.__ratings=rate
    def getRatings(self):return self.__ratings
    

'''
com1=Corporate()
com1.setOrg("Cognizant");com1.setNature("Service");com1.setOpennings("java");com1.setEmployees(10000);com1.setMinSal(3.9);com1.setPlace("chennai");com1.setRatings(4.2)
#print(com1.getEmployees(),com1.getMinSal(),com1.getNature(),com1.getOpnnings(),com1.getOrg(),com1.getPlace(),com1.getRatings())
res=com1
print(res)

com2=Corporate("ZOHO","Product","C","Chennai",21000,5.6,4.5)
print(com2.getEmployees(),com2.getMinSal(),com2.getNature(),com2.getOpnnings(),com2.getOrg(),com2.getPlace(),com2.getRatings())'''