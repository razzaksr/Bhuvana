# inheritance: class Derived(SuperClass):

# single, multi level, hierarchy, multiple, hybrid


class Google:
    def __init__(self,user="",email="",con=0):
        print("Google contructed")
        self.username=user
        self.email=email
        self.contact=con
    def __str__(self):
        return "Account Info "+self.username+" and "+self.email+" and "+str(self.contact)+"\n"

class PlayStore(Google):#single inheritance
    available=['free fire','whatsapp','facebook','instagram','gpay','phonepay','gmail','adobe','vlc','office','myjio']
    def __init__(self,name="",email="",con=0):
        print("Play store contructed")
        super(PlayStore,self).__init__(name,email,con)
        self.__downloads=[]
        self.__rated={}
    
    def getdownloads(self):
        return self.__downloads
    
    def getrates(self):
        return self.__rated
        
    def __gt__(self,name):
        if name in self.available:
            self.__downloads.append(name)
            print(name,"has downloaded")
        else:
            print(name,"is not in the play store")
    
    def __lt__(self,name):
        if name in self.__downloads:
            rate=float(input("Rate the "+name+":"))
            self.__rated[name]=rate
            print(name,"has rated as",rate,"by",self.username)
        else:
            print(name,"app not you have installed")
    

'''play=PlayStore("bhuvana","bhuvana@gmail.com",9654565434)
print(play)
play>'pubg'
play>'free fire'
play>'vlc'
play>'whatsapp'
play>'instagram'

play<'facebook'
play<'vlc'
'''


class Cloud(PlayStore): # multi level 
    def __init__(self, name="", email="", con=0):
        super().__init__(name, email, con)
    
    def myDownloads(self):
        print("Following apps are downloaded by",self.username)
        for x in self.getdownloads():
            print(x)
    
    def myRates(self):
        print("Following apps are rated by",self.username)
        for x,y in self.getrates().items():
            print(x,y)
    
    def __sub__(self,name):
        if name in self.getdownloads():
            self.getdownloads().remove(name)
            print(name,"app has uninstalled from your phone")
        else:
            print(name,"app not in your phone")
    def __str__(self):
        return str(super().__str__())+" "+str(self.getdownloads())+" "+str(self.getrates())+"\n"
'''    
cloud1=Cloud("razakmohamed","razzaksr@gmail.com",87654567873)
cloud1>'instagram'
cloud1>'office'
cloud1>'vlc'

cloud1.myDownloads()
cloud1<'office'
cloud1<'facebook'
cloud1<'instagram'

cloud1.myRates()

cloud1-'office'
cloud1-'free fire'

print(cloud1)

'''