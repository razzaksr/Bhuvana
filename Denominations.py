# denominations

_2000s,_500s,_200s,_100s=5,10,50,50

#print((_2000s*2000)+(_500s*500)+(_200s*200)+(_100s*100))

users=int(input("Tell us required cash: "))

user=users

output=""

_t2000s,_t500s,_t200s,_t100s=_2000s,_500s,_200s,_100s

if user>0 and user//2000!=0:
    count=user//2000
    if count<=_t2000s:
        _t2000s-=count
        user-=(count*2000)
        output="2000 X "+str(count)+"\n"
    
    else:
        output="2000 X "+str(_t2000s)+"\n"
        user-=(_t2000s*2000)
        _t2000s=0

if user>0 and _t500s>0:
    count=user//500
    if count<=_t500s:
        _t500s-=count
        user-=(count*500)
        output+="500 X "+str(count)+"\n"
    
    else:
        output+="500 X "+str(_t500s)+"\n"
        user-=(_t500s*500)
        _t500s=0

if user>0 and _t200s>0:
    count=user//200
    if count<=_t200s:
        _t200s-=count
        user-=(count*200)
        output+="200 X "+str(count)+"\n"
    
    else:
        output+="200 X "+str(_t200s)+"\n"
        user-=(_t200s*200)
        _t200s=0

if user>0 and _t100s>0:
    count=user//100
    if count<=_t100s:
        _t100s-=count
        user-=(count*100)
        output+="100 X "+str(count)+"\n"
    
    else:
        output+="100 X "+str(_t100s)+"\n"
        user-=(_t100s*100)
        _t100s=0

if user>0:
    _t2000s,_t500s,_t200s,_t100s=_2000s,_500s,_200s,_100s
    print(users," Required amount can't dispense")
elif user==0 and users>0:
    _2000s,_500s,_200s,_100s=_t2000s,_t500s,_t200s,_t100s
    print(users,"Required cash dispensed",output)
else:
    print("Invalid Cash required")