# -	Install DBMS (mysql)
# -	Pip install mysql
# -	Pip install mysql-connector
# -	Pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(host='localhost', user='root',
                                   passwd='gianmysql')
cursorObject = dataBase.cursor()  # prepare a cursor object
cursorObject.execute("CREATE DATABASE elderco")  # create a database
print("All done!")
