class BhuvanaError(RuntimeError):
    def __str__(self):
        return "Value is Not found anywhere"

hai={
    "Spring":["MVC","Core","AOP","jdbc","security","cloud"],
    "DJango":["Jinja","python","ORM"],
    "MERN":["Mongodb","Express","React","Node"],
    "Dotnet":["Angular","C#","Entity framework"]
}

def find():
    try:
        val=input("Tell us skill: ")
        for k,v in hai.items():
            if val in v:
                print(k,"contains",val)
                return
        raise BhuvanaError()
    except BhuvanaError as b:
        print(b)
        find()
        
find()