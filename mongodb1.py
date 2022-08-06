
import pymongo
client = pymongo.MongoClient("mongodb+srv://vish9868:Patilvish9868@cluster0.mlebtjg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

{
    "name": "vishwa",
    "email": "vishwanathpatil023@gmail.com",
    "surname": "patil"
}
db1 = client['pythonProject1']
coll = db1['test']
coll.insert_one(d)

{
    "name": "vishwa",
    "email": "vishwanathpatil023@gmail.com",
    "surname": "patil"
}

{
    "name": "vishwa",
    "email": "vishwanathpatil023@gmail.com",
    "surname": "patil"
}
