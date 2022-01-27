from pymysql import *

db=connect(host="localhost",user="root",password="")

qry="create database bhuvana"

cur=db.cursor()

cur.execute(qry)

db.close()

print("Database has created")