# sortings: bubble selection quick

from array import *

my_array=array('i',[98,12,45,76,89,13,7,4,12,65,33,72,81])
my_list=[9,2,8,3,4,67,9,12,6,54,8,11,9,3,4,98,3,1,4,5,12,7]
my_dict={
    2019:["python","javascript","java","dotnet"],
    2012:["java","dot ent","php"],
    2020:["python","java","javascript"],
    2021:["java","python","javascript","dotnet"],
    2010:["java","c","cpp","dotnet"]
}

def bubble(store):
    for times in range(len(store)):
        for com in range(len(store)-times-1):
            if store[com]>store[com+1]:
                store[com]*=store[com+1]
                store[com+1]=store[com]//store[com+1]
                store[com]//=store[com+1]

def selection(store):
    for select in range(len(store)):
        for com in range(select+1,len(store)):
            if store[select]<store[com]:
                store[select]^=store[com]
                store[com]^=store[select]
                store[select]^=store[com]
            

def iterate(store):
    for x in store:
        print(x,end=" ")
    print()

def split(store,start,end):
    pi_pos=start
    pi_data=store[pi_pos]
    
    while start<end:
        
        while start<len(store) and store[start]<=pi_data:
            start+=1
            
        while store[end]>pi_data:
            end-=1
        
        #swap
        if start<end:
            store[start],store[end]=store[end],store[start]
    
    store[end],store[pi_pos]=store[pi_pos],store[end]
    
    return end
        
def quick(store,start,end):
    if start<end:
        pivot=split(store,start,end)
        quick(store,start,pivot-1)
        quick(store,pivot+1,end)

#bubble(my_array)
#bubble(my_list)
#selection(my_array)
#selection(my_list)


iterate(my_array)
iterate(my_list)

quick(my_array,0,len(my_array)-1)
quick(my_list,0,len(my_list)-1)

iterate(my_array)
iterate(my_list)
