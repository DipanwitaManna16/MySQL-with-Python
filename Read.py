import mysql.connector
#Establishing the connection between python application & DB Server
mydb = mysql.connector.connect(host="localhost",user="root" ,passwd="Dipanwita@123",database="demo")
mycursor = mydb.cursor()
mycursor.execute('Select name from employee')
myresult1 = mycursor.fetchone()            # fetch or read one value name from employee table

#print result
for row in myresult1:
    print(row)

myresult2 = mycursor.fetchall()            # fetch or read all values name from employee table
#print result
for row in myresult2:
    print(row)