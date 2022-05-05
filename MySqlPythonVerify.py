
# This code
# shows one can execute MariaDB instructions from python
# using the just installed MySql python connector interface

# the next helper function make it easy the execution of coomands in 
# the mariadb client

def ExecMariaDBcmd(thecmd):
    cursor.execute(thecmd)
    return cursor.fetchall()

import sys
import mysql.connector as mydbase

# Connect to MariaDB Platform
try:
    connection = mydbase.connect(
        user="mypytest",
        password="iam",
        host="127.0.0.1",
        port=3306,
        database="test"
    )
except mydbase.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get a cursor
cursor = connection.cursor()

res = ExecMariaDBcmd("SELECT VERSION()")
print("This is version {0} Python/connector".format(res[0][0]))

res = ExecMariaDBcmd("SHOW VARIABLES WHERE variable_name = 'version'")
print("This is {0} {1} Python/connector".format(res[0][0],res[0][1]))

res = ExecMariaDBcmd("SELECT CURDATE()")
print("Today's date is: {0}".format(str(res[0][0])))

res = ExecMariaDBcmd("SHOW VARIABLES WHERE Variable_Name LIKE '%datadir%'")
print("The {0} for this server is at {1}".format(res[0][0],res[0][1]))

res = ExecMariaDBcmd("SELECT USER(),CURRENT_USER()")
print("The current user is: {0}".format(res[0][0]))

res = ExecMariaDBcmd("SHOW TABLES FROM test")
print("The database 'test' contains '{0}'".format(res[0][0]))

cursor.execute("USE test")

res = ExecMariaDBcmd("SHOW TABLES")
print("The database 'test' contains '{0}'".format(res[0][0]))

res = ExecMariaDBcmd("DESCRIBE books")
print("The fields in 'books' are: ")
for i in res:
    print(i)

res = ExecMariaDBcmd("SELECT * FROM books")
print("Current items in 'books' are: ")
for i in res:
    print(i)

print(" The following items will be added to 'books': ")
print('cursor.execute("INSERT INTO books VALUES(444,'+"'MySQL Connector Python 444'," +' 444)")')
print('cursor.execute("INSERT INTO books VALUES(555,'+"'MySQL Connector Python 555'," +' 555)")')

cursor.execute("INSERT INTO books VALUES(444, 'MySQL Connector Python 444', 444)")
connection.commit()
cursor.execute("INSERT INTO books VALUES(555, 'MySQL Connector Python 555', 555)")
connection.commit()

res = ExecMariaDBcmd("SELECT * FROM books")
print("Now Current items in 'books' are: ")
for i in res:
    print(i)

# Always close a session
cursor.close()
connection.close()

