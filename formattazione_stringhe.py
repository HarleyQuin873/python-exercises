#Creare due variabili "nome" e "cognome" e concatenarle a schermo.
nome="Marina"
cognome="Pugliese"
print(nome + " " + cognome)

#Utilizzare la formattazione delle stringhe per ottenere "Il numero è: 42".
numero=42
stringa='Il numero è: {}'.format(numero)

print(stringa)

#Utilizzare la formattazione delle stringhe per ottenere
#  "Il numero binario di 42 è 0b101010". Per il binario utilizzare bin(numero)

s='Il numero binario di {} è {}'.format(numero, bin(numero))
print(s)

#Partendo dalla variabile "numero" uguale a 5, utilizzare 
# le f-strings (interpolazione) per ottenere "Il quadrato di 5 è 25".

numero=5
str1="Il quadrato di {} è {}".format(numero,numero*numero)
print(str1)

str2=f"Il quadrato di {numero} è {numero ** 2}"
print(str2)

#Partendo da "nome" e "cognome" utilizzare la formattazione strighe per 
# ottenere "Il mio nome è {nome} ed il cognome è {cognome}". 
# Come da esempio dovete fare riferimento al nome delle variabili e non alla posizione usata dentro format.

#str="Il mio nome è {" + nome +"} ed il cognome è {" + cognome + "}"
print(str)

str2="Il mio nome è {nome} ed il cognome è {cognome}".format(nome=nome, cognome=cognome)
print(str2)

#Facendo riferimento all'esercizio precedente ottenere il 
# seguente risultato modificando i valori nel format(): "Il mio nome è LUCA ed il cognome è RoKKi"

str3="Il mio nome è {nome} ed il cognome è {cognome}".format(nome='LUCA', cognome='RoKKi')
print(str3)
