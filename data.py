import pymongo

client = pymongo.MongoClient('mongodb://www.shehzikhan.ml:27017')
db=client['datavis']
collection=db['cellphone-specs']

for i,x in enumerate(collection.find().distinct("brand")):
    print(i,x,len(collection.find({"brand":x})))
