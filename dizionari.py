#Creare un dizionario vuoto e assegnarlo a una variabile.

d={}
print(d)

#Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.

d={
    "nome" : "Mario",
    "cognome" : "Rossi",
    "età" : "30"
}
print(d)

#Accedere al valore dell'elemento con chiave "età" del dizionario precedente.
età=d["età"]
print(età)

#Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.

#d.update("email": "mario.rossi@email.com")
d["email"]="mario.rossi@email.com"
print(d)

#Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.

del d["cognome"]
print(d)

#Creare una nuova lista che contenga solo le chiavi del dizionario precedente.

#l=[d["nome"], d["età"], d["email"]]
chiavi=list(d.keys())
print(chiavi)

#Creare una nuova lista che contenga solo i valori del dizionario precedente.
valori= list(d.values())
print(valori)

#Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.
d["età"]=35
print(d)

#Contare il numero di elementi nel dizionario precedente.
n=len(d)
print(n)