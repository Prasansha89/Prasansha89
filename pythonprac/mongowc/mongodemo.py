#library or module for mongodb
from pymongo import MongoClient
#for connection establishment 
client=MongoClient("mongodb://localhost:27017")
#databse name
mydb=client["itsdb"]
#colection
mycollection=mydb["Student info"]
#insert data into collection for many records insert_many

'''mycollection.insert_one({"Name":"Pawan","email":"p@gmail.com","course":"BCA" })'''
#data visible in mongo compass is in the format of json ......{"Name":"Pawan","email":"p@gmail.com","course":"BCA" } know as document in mongo

'''mycollection.insert_many([{"Name":"Pawan","email":"p@gmail.com","course":"BCA"},{"Name":"Rahul","email":"ra@gmail.com","course":"BBA"}])'''
# to fetch the data
'''data=mycollection.find()
for student in data:
    print(student)'''

# to fetch specific record find_one return single record
'''data=mycollection.find_one({"email":"p@gmail.com"})
print(data)'''

#to delete data
'''mycollection.delete_one({"email":"p@gmail.com"})'''
#to delete many data mycollection.dalate_many([{})

#to update the exixting data
mycollection.update_one({"course":"BCA"},{"$set":{"course":"Bechalor od computer application"}})