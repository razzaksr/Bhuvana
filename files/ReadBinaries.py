from pickle import *

file=open("D:\\Course backups\\Python\\bins.doc","rb")

hai=load(file)

for item in hai:
    print(item)

file.close()