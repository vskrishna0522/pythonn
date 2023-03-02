import pymongo
import json
client = pymongo.MongoClient()
db = client['pydata']
collection = db['emp1']
with open('C:/Users/mypc/Downloads/data.json') as f:
    data = json.load(f)
    collection.insert_many(data)
#print(data)
r = collection.find_one({"id": 999})
for doc in r:
  print(r)
#list(map(print,r))