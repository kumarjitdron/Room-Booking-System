import mysql.connector as a
mydb=a.connect(
	host='localhost',
	user='root',
	password='Password',#Enter your sql password here!!!
	database='rms')
cur=mydb.cursor()
def checkin():
	print("1. Update Check In ")
	print("2. View Checked In ")
	c=int(input("Choice: "))
	if c==1:
		d=input("Days: ")
		n=input("Name: ")
		a=input("Adhaar: ")
		dt=input("Date: ")
		t=input("Type & Number: ")
		sql="insert into checkin values(%s,%s,%s,%s,%s)"
		data=(d,n,a,dt,t)
		cur.execute(sql,data)
		mydb.commit()
		print("Data Entered sucessfully!!")
		main()
	elif c==2:
		s="select * from checkin"
		cur.execute(s)
		d=cur.fetchall()
		for i in d:
			print(i)
		main()
	else:
		print("Enter Correct option!!")
		main()
def checkout():
	print("1. Update Check Out ")
	print("2. View Checked Out ")
	c=int(input("Choice: "))
	if c==1:
		b=input("Type & number: ")
		g=int(input("Guests: "))
		f=int(input("Fare: "))
		d=int(input("Days: "))
		tbill=g*f*d
		dt=input("Date: ")
		data=(b,g,f,d,tbill,dt)
		sql="insert into checkout values(%s,%s,%s,%s,%s,%s)"
		cur.execute(sql,data)
		mydb.commit()
		print("Data Entered Sucessfully!!")
		main()
	elif c==2:
		s="select * from checkout"
		cur.execute(s)
		d=cur.fetchall()
		for i in d:
			print(i)
		main()
	else:
		print("Enter Correct option!!")
		main()

def rooms():
	print("Executive - 5000/d/guests")
	print(" ")
	print('''Facilities- Wifi , T.V., AC, Geyser in Bathrom ,
		Breakfast,lunch,dinner''')
	print(" ")
	print("Deluxe - 2500/d/guests")
	print(" ")
	print('''Facilities- Wifi , T.V., Non-AC, Geyser in Bathrom, dinner ,lunch  ''')
	print(" ")
	print("Simple - 1000/d/g")
	print(" ")
	print('''Facilities- Wifi , T.V., Non-AC, Geyser in Bathrom''')
	main()
def main():
	print("1. Check In ")
	print("2. Check Out ")
	print("3. Fare and Amenities ")
	c=int(input("Choice: "))
	if c==1:
		checkin()
	elif c==2:
		checkout()
	elif c==3:
		rooms()
	else:
		print("Enter Correct Choice!!!")
	main()
main()

