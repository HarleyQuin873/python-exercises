#Scrivi un programma che stampa la data e l'ora corrente

import datetime

ora = datetime.datetime.now()
print("Data e ora corrente: ",ora)

#Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e stampa il nome del mese corrispondente.
data = input("Inserisci una data (gg/mm/aaaa): ")
data = datetime.datetime.strptime(data, "%d/%m/%Y")

nome_mese = data.strftime("%B")
print("Il nome del mese corrispondente è:", nome_mese)

#Scrivi un programma che prende in input due date e calcola la differenza in giorni tra le due.

data1 = input("Inserisci la prima data (gg/mm/aaaa): ")
data2 = input("Inserisci la prima data (gg/mm/aaaa): ")

data1 = datetime.datetime.strptime(data1, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data2, "%d/%m/%Y")

diff = abs(data2 - data1).days
print("La differenza in giorni tra le due date è:", diff)

#Scrivi un programma che prende in input una data e un numero di giorni, e calcola la data che viene dopo quella data del numero di giorni specificato.

data3 = input("Inserisci una data (gg/mm/aaaa): ")
num_giorni = int(input("Inserisci il numero di giorni: "))

data3 = datetime.datetime.strptime(data, "%d/%m/%Y")
nuova_data = data + datetime.timedelta(days=num_giorni)

print("La nuova data è:", nuova_data.strftime("%d/%m/%Y"))


















   

