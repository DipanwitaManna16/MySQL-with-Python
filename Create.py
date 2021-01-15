import mysql.connector
#Establishing the connection between python application & DB Server
mydb = mysql.connector.connect(host="localhost",user="root" ,passwd="Dipanwita@123",database="demo")
mycursor = mydb.cursor()
#------------------------CREATE---------------------------#

#mycursor.execute('Create table employee(Name varchar(20) , Salary int(20) )')
mycursor.execute('Show tables')

#Print table
for tb in mycursor:
    print(tb)