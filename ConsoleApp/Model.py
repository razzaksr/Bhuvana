class Corporate:
    __org,__nature,__opennings,__place,__employees,__minSal,__ratings="","","","",0,0.0,0.0
    
    def __init__(self,org="",nature="",open="",plc="",emp=0,sal=0.0,rate=0.0):
        self.__org=org;self.__nature=nature;self.__opennings=open;self.__place=plc;self.__employees=emp
        self.__minSal=sal;self.__ratings=rate
    
    def __str__(self):
        return "Corporate name "+self.__org+" is "+self.__nature+" company has ratings among people "+str(self.__ratings)+" in "+self.__place+" has resources of "+str(self.__employees)+" has offering jobs on "+self.__opennings+" with basic pay of "+str(self.__minSal)+"\n";
    
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