from pymongo import MongoClient

#create connection with mongodb
client = MongoClient("mongodb://localhost:27017")

#creatae new database in mongodb
mydatabase = client["libdb"]

#create new collection in database
mycollection = mydatabase["addbook"]