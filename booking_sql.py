import mysql.connector as a
mydb=a.connect(
	host='localhost',
	user='root',
	password='9507910150')
cur=mydb.cursor()
s="create database rms;"
cur.execute(s)
s1="use rms;"
cur.execute(s1)
s2="create table checkin(day varchar(50),name varchar(50),aadhar varchar(20),date varchar(30),typenumber varchar(50))"
cur.execute(s2)
s3="create table checkout(typenumber varchar(50),gurests integer,fare integer,days integer,tbill integer,date varchar(20))"
cur.execute(s3)
mydb.commit()