import mysql.connector
#Establishing the connection between python application & DB Server
mydb = mysql.connector.connect(host="localhost",user="root" ,passwd="Dipanwita@123",database="demo")
mycursor = mydb.cursor()

sqlform = 'Update employee set salary = 10500 where name = "harshita" '
mycursor.execute(sqlform)
mydb.commit()

#Checking the new updated values
mycursor.execute('Select salary from employee where name="harshita" ')
myresult = mycursor.fetchone()            # fetch or read all values name from employee table
#print result
for row in myresult:
    print(row)