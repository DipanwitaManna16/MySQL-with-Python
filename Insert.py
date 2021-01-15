import mysql.connector
#Establishing the connection between python application & DB Server
mydb = mysql.connector.connect(host="localhost",user="root" ,passwd="Dipanwita@123",database="demo")
mycursor = mydb.cursor()
#------------------------INSERT----------------------
sqlform = 'Insert into employee(name,salary) values(%s,%s)'

#list of tuples to insert the values
employees = [('harshita',10000) ,('rivan',11000) ,('niharika',11500) ,('pradip',9500),('palash',15000),('sudhir',12700) ]

mycursor.executemany(sqlform,employees)
mydb.commit()