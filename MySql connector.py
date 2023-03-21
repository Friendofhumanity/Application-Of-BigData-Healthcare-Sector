"""import mysql.connector 
import connection
 
 

conn = mysql.connector.connect(user = 'infinity', password = 'mahi' ,   host = 'localhost',
                              database = 'Health')
 
print(conn)
 """




# Python program to connect
# to mysql database


from mysql.connector import connection


dict = {
'user' : 'root',
'host' : 'localhost',
'database' : 'Health' ,
'password' : 'mahi0'}

# Connecting to the server
conn = connection.MySQLConnection(**dict)

print(conn)

# Disconnecting from the server
conn.close()
