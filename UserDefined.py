# user defined function

def migrate():
    print("Simple function without param and return")

def current(skill="c"):
    if skill == 'java':print(skill,"Opennings in Spring")
    elif skill == 'python':print(skill,"Opennings in Flask")
    elif skill == 'javascript':print(skill,"Opennings in React")
    else:print("No opennings in",skill)

def consultant(exp,tech):
    if exp>=8 and tech == 'python' or tech=='javascript':
        print("You are recruited as Consultant")
    else:
        print("Try after sometime")

def manage():
    count=int(input("Tell us count: "))
    if count<2:
        #return
        return "Invalid limit for fibonacci"
    else:
        chk=""
        num1=0
        num2=1
        chk+=" "+str(num1)
        chk+=" "+str(num2)
        #print(num1)
        #print(num2)
        count-=2
        for x in range(1,count+1):
            sum=num1+num2
            chk+=" "+str(sum)
            num1=num2
            num2=sum
        return chk


def find(category):
    movies={
        "drama":["Soorari Potru","Karnan"],
        "thriller":["Maanaadu","Thadam","Mercury"],
        "horror":["Pizza","2.0","Nejam marapathillai"]
    }
    
    return movies[category][0]
    
        
'''
migrate()
current()
current("java")
consultant(9,'php')
consultant(tech="python",exp=8)
#manage()
res=manage()
print(res)

yet=find("thriller")
print(yet)'''