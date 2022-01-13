# file properties and opnning and closing an file
# modes>> w, r, a, wb,rb,ab

# w mode create file not exists , replace if exists
hey=open("D:\\Course backups\\Python\\bhuvana.xls","w")
print(hey.name)
print(hey.closed)
hai=input("Any content write to file:")
hey.write(hai)
hey.close()
print(hey.closed)