
#install mysql on your computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python



import mysql.connector 
database = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd='root',
)

#prepare a cursor object
cursorObject  = database.cursor()

#create a database in local mysql workbench
cursorObject.execute('CREATE DATABASE elderco')

print('Database created with name elderco')