from pymysql import *

db=connect(host="localhost",user="root",password="",database="bhuvana")

#table creation
#qry="create table corporate(org varchar(250) not null, nature varchar(250) not null, opennings text not null, place text not null, employees int(4) not null, basic float not null, ratings float not null)"

#adding primary key
qry="alter table corporate add primary key(org)"

cur=db.cursor()

cur.execute(qry)

db.close()

#print("Table has created")

print("Primary key added")