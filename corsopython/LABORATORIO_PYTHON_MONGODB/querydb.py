import pymongo
from pymongo import MongoClient

#ESEGUO la connessione con mongo db
#clent = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:*****/')

#accedo a  un db e lo chiamo testdb
db = client.testdb

#accesso alla collection persone
persone_coll = db.persone

p= persone_coll.find_one()
print(p)

print("***")
persone = persone_coll.find({"computer":"apple"})
for persona in persone:
    print(persona)


#MODIFICA DI UN documento
print("****")
res = persone_coll.update_one({"nome":"Giuseppe"}, {"$set": {"eta": 50}})
p= persone_coll.find_one({"nome":"Giuseppe"})
print(p)

#filtro
#nome maggiore di > Giuseppe ---->$gt
print("*****")
persona = persone_coll.find_one({"nome" : {"$gt": "Giuseppe"}})
print(persona)
