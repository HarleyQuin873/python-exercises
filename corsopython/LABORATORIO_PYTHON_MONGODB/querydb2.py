import pymongo
from pymongo import MongoClient

#eseguo la connessione
client = MongoClient('mongodb://localhost:*****/')

#accedo a un db e lo chiamo testdb
db = client.testdb

#accesso alla collection persone
persone_coll = db.persone

#Trovo il primo documento nella collection 'persone' (se esiste)
# 'find_one()' restituisce il primo documento che trova nella collection
p = persone_coll.find_one()
print(p)

print("***")
# Trovo tutti i documenti nella collection 'persone' dove il campo 'computer' contiene "apple"
# 'find()' restituisce un cursore che può essere iterato per ottenere tutti i documenti che corrispondono alla query
persone = persone_coll.find({"computer":"apple"})
for persona in persone:
    print(persona)

#modifica di un documento
print("****")
# 'update_one()' aggiorna il primo documento che trova che corrisponde al filtro
# In questo caso, stiamo cercando il documento dove 'nome' è uguale a "Giuseppe"
# Aggiorniamo il campo 'eta' a 50
res = persone_coll.update_one({"nome":"Giuseppe"}, {"$set": {"eta":50}})
# Trovo il documento aggiornato con nome "Giuseppe"
persone = persone_coll.find_one({"nome":"Giuseppe"})
print(persone)

#filtro
#nome maggiore di > Giuseppe ---->$gt
# Filtro con l'operatore $gt
# Troviamo il primo documento dove 'nome' è maggiore di "Giuseppe"
# L'operatore $gt (greater than) confronta i valori
print("*****")
persona = persone_coll.find_one({"nome" : {"$gt" : "Giuseppe"}})
print(persona)