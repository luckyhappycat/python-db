import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["pyframe-test"]
print(db)

dblist = client.list_database_names()
print(dblist)


var = {"path": "/data"}
collection = db["environ"]
ret = collection.insert_one(var)
print(ret.inserted_id)
