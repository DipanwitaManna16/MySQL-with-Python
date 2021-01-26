import mysql.connector
#Establishing the connection between python application & DB Server
mydb = mysql.connector.connect(host="localhost",user="root" ,passwd="Dipanwita@123",database="demo")
mycursor = mydb.cursor()


sqlform = 'Delete from employee where name = "pradip" '
mycursor.execute(sqlform)
mydb.commit()

#Checking the new updated values
mycursor.execute('Select * from employee')
myresult = mycursor.fetchall()            # fetch or read all values name from employee table
#print result
for row in myresult:
    print(row)