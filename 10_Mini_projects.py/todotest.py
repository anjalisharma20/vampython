import mysql.connector

#establish the database connection in between python to mysql
connection = mysql.connector.connect(host = "localhost",username = "root",password = "12345678", database = "todo")

#to verify the connection is establish or not
if connection.is_connected():
    print("db is connect")
else:
    print("db not connect")
    
# #create table in database
# createQuery = "create table if not exists subscribers (name text, email text)"

# #to execute the mysql queries with cursor
# mycursor = connection.cursor()

# #to execute the mysql create query
# mycursor.execute(createQuery)
# connection.commit()

# #add new records in database
# # insertQuery = "insert into subscribers values('{}', '{}')".format(input('enter name'), input('enter email'))
# # mycursor.execute(insertQuery)
# # connection.commit()

# #retrive the records from database3
# # selectQuery = "select * from subscribers"
# # mycursor.execute(selectQuery)
# # for record in mycursor.fetchall():
# #     print(record)
# # connection.commit()

# #retrive the specific records with the help of where
# # whereQuery = "select * from subscribers where email='p@gmail.com'"
# # mycursor.execute(whereQuery)
# # print(mycursor.fetchall())

# #update the records in database
# # updateQuery = "update subscribers set name ='Rahul Sharma' where email = 'p@gmail.com'"
# # mycursor.execute(updateQuery)
# # connection.commit()

# #delete the records from database
# # deleteQuery = "delete from subscribers where email = 'p@gmail.com'"
# # mycursor.execute(deleteQuery)
# # connection.commit()

# #drop the table in database
# dropQuery = "drop table subscribers"
# mycursor.execute(dropQuery)
# connection.commit()
