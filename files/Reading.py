# reading an file with r mode

file=open("D:\\Course backups\\Javascript\\Manikandan\\Websocket\\day one\\SocketServer\\index.js","r")

#data=file.read() # read everything
#data=file.read(100) # read specific amount of characters
file.seek(110,0)
pos=file.tell()
print(pos," where cursor is now pointing")
data=file.read(pos) # seek to locate cursor somewhere and read




print(data)

file.close()