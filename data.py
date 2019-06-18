import pymongo

client = pymongo.MongoClient('mongodb://www.shehzikhan.ml:27017')
db=client['datavis']
collection=db['cellphone-specs']

print(collection.find_one().keys())
exit()
for i,x in enumerate(collection.keys()):
    print(i,x,len(collection.find({"brand":x})))
