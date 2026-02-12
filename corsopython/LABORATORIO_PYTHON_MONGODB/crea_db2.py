import pymongo
from pymongo import MongoClient

# Questa riga stabilisce una connessione a MongoDB che si trova in esecuzione sulla macchina locale (localhost) sulla porta predefinita 27017. Se MongoDB è installato e in esecuzione, questa riga stabilisce la connessione al server.
client = MongoClient('mongodb://localhost:*****/')

#creo un db e lo chiamo testdb
db = client.testdb ##Qui stai creando un database chiamato testdb. Se il database non esiste, MongoDB lo creerà automaticamente al momento del primo utilizzo.

#creo la collection persone
persone_coll = db.persone #Con questa riga stai creando una collection chiamata persone nel database testdb. Le collections sono simili alle tabelle in un database relazionale.


#Queste righe creano degli indici per le proprietà nome, cognome e computer dei documenti nella collection persone. Gli indici permettono di velocizzare le operazioni di ricerca su questi campi.
persone_coll.create_index([("nome", pymongo.ASCENDING)])
persone_coll.create_index([("cognome", pymongo.ASCENDING)])
persone_coll.create_index([("computer", pymongo.ASCENDING)])

#creo un documento
p1 = {
    "nome":"Mario", 
    "cognome":"Rossi", 
    "eta":30, 
    "computer":["asus", "apple"]
    }
#Qui crei due documenti (dizionari Python) che rappresentano persone con un nome, cognome, età e una lista di computer. Questi documenti vengono quindi inseriti nella collection persone.

#inseriamo il documento in mongodb
persone_coll.insert_one(p1)

p2 = {
    "nome":"Giuseppe", 
    "cognome":"Verdi", 
    "eta":45, 
    "computer":["apple"]
    }

persone_coll.insert_one(p2)

