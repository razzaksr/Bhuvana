# dictionary:

hai={
    "Spring":["MVC","Core","AOP","jdbc","security","cloud"],
    "DJango":["Jinja","python","ORM"],
    "MERN":["Mongodb","Express","React","Node"],
    "Dotnet":["Angular","C#","Entity framework"]
}

def extract(chance=1):
    try:
        print(hai[input("Enter the skillset: ")])
    except KeyError as ke:
        print(ke,"\nInvalid skill")
        if chance<=2:
            extract(chance+1)
        
extract()