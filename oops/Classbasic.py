class Hai:
    alpha=0 
    beta=0
    def perform(self):
        print(self.alpha&self.beta)

h=Hai()
h.alpha=120
h.beta=90
h.perform()

y=Hai()
y.alpha=879
y.beta=122
y.perform()

class Hey:
    __sigma=0
    __delta=0
    
    def setSigma(self,data):
        self.__sigma=data
    def getSigma(self):
        return self.__sigma
    
one=Hey()
#print(one.__delta,one.__sigma)
one.setSigma(120)
print(one.getSigma())
    