from pickle import *

skillset={"web":["java","javascript"],
          "mobile":["android"],
          "desktop":["java"]}

yet={34.6,90.4,76.4,12.5,23.6,87.5,78.4,120.5,34.6,90.4,12.5}

hai=(87,34,90,11,45,76,34,12,20,87,55,54,87)

hello=["vikas","varun","balaji","hemsworth","vanathi","holland","aarthi"]

file=open("D:\\Course backups\\Python\\bins.doc","wb")

'''
# pickling
encry=dumps(skillset)

print(encry)

#unpickling
print(loads(encry))

file.write(encry)
'''


# pickling
#dump(skillset,file)
dump(yet,file)

file.close()