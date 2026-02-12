import pymongo
from pymongo import MongoClient

#ESEGUO la connessione con mongo db
#clent = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:*****/')

#creo un db e lo chiamo testdb
db = client.testdb

#creo la collection persone
persone_coll = db.persone

persone_coll.create_index([("nome", pymongo.ASCENDING)])
persone_coll.create_index([("cognome", pymongo.ASCENDING)])
persone_coll.create_index([("computer", pymongo.ASCENDING)])

#creo un documento
p1 = {"nome":"Mario", "cognome":"Rossi", "eta":30, 
        "computer":["asus", "apple"]}

#inseriamo il documento in mongodb
persone_coll.insert_one(p1)

p2 = {"nome":"Giuseppe", "cognome":"Verdi", "eta":45, 
        "computer":["apple"]}

persone_coll.insert_one(p2)







