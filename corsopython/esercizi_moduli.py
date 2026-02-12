import math

radice = math.sqrt(16)
print(radice)

#Importa il modulo random e genera un numero casuale compreso tra 1 e 10..

import random

nc = random.randint(1,10)
print(nc)

#Crea un nuovo file Python chiamato mio_modulo.py e definisci una funzione chiamata somma che prende due argomenti e restituisce la loro somma. Poi importa il modulo nel tuo programma principale e usa la funzione somma.
import mio_modulo
s =mio_modulo.somma(34,765675)
print(s)

#Crea un nuovo file Python chiamato altro_modulo.py e definisci una variabile chiamata lista_numeri che contiene una lista di numeri interi. Poi importa il modulo nel tuo programma principale e stampa la lista.
import altro_modulo
print(altro_modulo.lista_numeri)

#Importa il modulo os e stampa la directory di lavoro corrente.
import os
print(os.getcwd())

#Importa il modulo datetime e stampa la data e l'ora corrente.

import datetime

ora =datetime.datetime.now()
print(ora)

#Crea un nuovo file Python chiamato esempio_pacchetto.py e mettilo in una cartella chiamata mio_pacchetto. All'interno di esempio_pacchetto.py, importa il modulo mio_modulo dal primo esercizio e usa la funzione somma. Poi importa il pacchetto nel tuo programma principale e usa la funzione somma.

import mio_pacchetto.esempio_pacchetto

s= mio_pacchetto.esempio_pacchetto.somma(67,54)
print(s)

#Importa il modulo csv e apri il file dati.csv che contiene una tabella di dati separati da virgola. Poi leggi il contenuto del file e stampalo.

import csv

with open('dati.csv', 'r') as file:
    lettore = csv.reader(file)
    for riga in lettore:
        print(riga)





#Importa il modulo json e crea un dizionario con alcune chiavi e valori. Poi serializza il dizionario in formato JSON e stampalo.

import json

dizionario = {'nome': 'Marco', 'cognome': 'Rossi', 'eta': 30}
json_dizionario = json.dumps(dizionario)

print(json_dizionario)
print(dizionario)






