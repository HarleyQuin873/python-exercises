import datetime

#Scrivi un programma che stampa la data e l'ora corrente

# ora = datetime.datetime.now()

# print("Data e ora corrente: ", ora)

#Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e stampa il nome del mese corrispondente.

# data = input("Inserisci una data( gg/mm/aaaa ): " )
# data = datetime.datetime.strptime(data, "%d/%m/%Y")

# print(data)

# nome_mese = data.strftime("%B")
# print("Il nome del mese corrispondente é: ", nome_mese)

#Scrivi un programma che prende in input due date e calcola la differenza in giorni tra le due.

data1 = input("Inserire prima data: ")
data1 = datetime.datetime.strptime(data1, "%d/%m/%Y")

data2 =  input("Inserire seconda data: ")
data2 = datetime.datetime.strptime(data2, "%d/%m/%Y")

diff= abs(data1-data2).days

print("La differenza in giorni tra le due date è: ", diff)

#Scrivi un programma che prende in input una data e un numero di giorni, e calcola la data che viene dopo quella data del numero di giorni specificato.

data3= input("Inserire una data nel formato gg/mm/aaaa: ")
data3= datetime.datetime.strptime(data3, "%d/%m/%Y")

giorni=int(input("Inserire numero di giorni per calcolare la prossima data: "))

data4= data3 + datetime.timedelta(days=giorni)
print("Data successiva trascorsi ", giorni, "è : ", data4)






