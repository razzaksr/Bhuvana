# relational : > >= < <= == !=  True/False

'''myOpennings={
    "java":{"web":[4.5,3.2,1.9,5.6],"test":[2.4,3.1]},
    "python":{"django":[5.6,3.5,2.2,4.7],"flask":[4.5,3.1,6.7]},
    "js":[5.6,9.2,4.5,10.4]
}
'''

'''
myOpennings={
    "web":4.5,"test":3.1,
    "django":3.5,"flask":6.7,
    "js":5.6
}
'''

'''
tech=input("Tell us technology: ")

print(tech in myOpennings)

expected=float(input("Tell us expected: "))

print("does it matched my expectation",myOpennings[tech]>=expected)'''


myJobs={
    9:["Project Manager","Solution Architect","Senior Consultant"],
    5:["Team Lead","Consultant","Senior Programmer"],
    2:["Developer","Associate Trainee","Trainee"]
}

exp=int(input("Tell us experience: "))

for x,y in myJobs.items():
    if x <= exp:
        role=input("Tell us desired role: ")
        if role in y:
            print(y," Found")
            break
        
