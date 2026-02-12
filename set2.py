#Creare un set vuoto e assegnarlo a una variabile.

s=()
print(s)

#Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".

insieme=set(["mela", "banana", "kiwi","mela"])
print(insieme)

#Aggiungere l'elemento "pesca" al set precedente.

insieme.add("pesca")

print(insieme)

#Rimuovere l'elemento "mela" dal set precedente.
insieme.remove("mela")
print(insieme)

#Verificare se l'elemento "ananas" è presente nel set precedente.

if "ananas" in insieme:
    print("L'elemento ananas è prensente nel set")
else:
    print("L'elemento ananas non è prensente nel set.")

#Creare un nuovo set contenente gli elementi "banana", "kiwi" e "arancia".

w= set(["banana", "kiwi", "arancia"])
print(w)

#Creare un set contenente i numeri interi da 1 a 5 ricavati da un range().

numeri=set(range(1,6))
print(numeri)

#Creare un nuovo set contenente i numeri pari del set precedente.

pari=[x for x in numeri  if x%2==0 ]

print(pari)