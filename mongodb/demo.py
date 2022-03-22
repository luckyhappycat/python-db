import os
import pymongo

client = pymongo.MongoClient("mongodb://172.17.50.89:27017/")

db = client["pyframe-test"]
print(db)

dblist = client.list_database_names()
print(dblist)

collection = db["environ"]

# find_one
primary_key = "build-3"
ret = collection.find_one(filter={"_id": primary_key})
if ret is None:
    print("{}不存在，准备插入".format(primary_key))
    # insert_one
    environment = {"_id": primary_key, "path": "/data", "version":"1.0.0"}
    ret = collection.insert_one(environment)
    print(ret.inserted_id)
else:
    print("{}存在".format(primary_key))

# update
collection.update_one()

# delete



# class Env:
#     def __init__(self, ip : str="172.17.50.89", port: int=27017) -> None:
#         self.ip = ip
#         self.port = port
#         self.client = pymongo.MongoClient("mongodb://{}:{}/".format(ip, port))
#         self.db = client['pyframe-test']
#         self.col = db["environ"]
#         self.pipelineid = "pipelineid"
#         self.pipeline_number = "1"
#         # self.pipelineid = os.environ["pipelineid"]
#         # self.pipeline_number = os.environ["pipeline_number"]

#     def exist(self):
#         ret = self.col.find_one({"_id": "{}_{}".format(self.pipelineid, self.pipeline_number)})
#         if ret is None:
#             return False
#         else:
#             return True

#     def set(self, environment: dict):
#         self.col.insert_one(environment)

#     def save(self):
#         pass

#     def get(self, key: str):
#         ret = self.col.find_one({"_id": "{}_{}".format(self.pipelineid, self.pipeline_number)})
#         if ret is not None:
#             return ret.get(key)
#         else:
#             environment = os.environ
#             return environment.get(key)


#     def load(self):
#         ret = self.col.find_one({"_id": "{}_{}".format(self.pipelineid, self.pipeline_number)})
#         return ret