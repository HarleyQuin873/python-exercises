#Creare due variabili "nome" e "cognome" e concatenarle a schermo.

nome ="Marina"
cognome="Pugliese"
# c=nome+cognome
# print(c)

#Utilizzare la formattazione delle stringhe per ottenere "Il numero è: 42".
# x="42"
# print("Il numero è: ", x)

# numero=42
# stringa='Il numero è: {}'.format(numero)
# print(stringa)

#Utilizzare la formattazione delle stringhe per ottenere
#  "Il numero binario di 42 è 0b101010". Per il binario utilizzare bin(numero)

# numero=42
# stringa='Il numero di {} è {}'.format(numero, bin(numero))
# print(stringa)

# n=43
# s='Il binario di {} è {}'.format(n, bin(n))
# print(s)

#Partendo dalla variabile "numero" uguale a 5, utilizzare 
# le f-strings (interpolazione) per ottenere "Il quadrato di 5 è 25".

# num=5
# # string='Il quadrato di {} è {}'.format(num, num*num)
# # print(string)

# s2=f'Il quadrato di {num} è {num**2}'
# print(s2)

#Partendo da "nome" e "cognome" utilizzare la formattazione strighe per 
# ottenere "Il mio nome è {nome} ed il cognome è {cognome}". 
# Come da esempio dovete fare riferimento al nome delle variabili e non alla posizione usata dentro format.

s3=f'Il mio nome è {nome} ed il cognome è {cognome}'
print(s3)

#Facendo riferimento all'esercizio precedente ottenere il 
# seguente risultato modificando i valori nel format(): "Il mio nome è LUCA ed il cognome è RoKKi"

s4='Il mio nome è {} ed il cognome è {}'.format(nome='LUCA', cognome='Rokki')
print(s4)