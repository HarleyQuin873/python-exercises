lista=[]
print(lista)

#Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.

l=[1,2,3,4,5]
print(l)

#Accedere all'elemento con indice 2 della lista precedente.

d=l[2]
print(d)

#Aggiungere un nuovo elemento "6" alla lista precedente.

l.append(6)
print(l)

#Rimuovere l'elemento con indice 3 dalla lista precedente

del l[3]
print(l)

#Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.

l2=l[:3]
print(l2)

#Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.

l3=l2[1]
print(l3)

dispari=[l[1::2]]
print(dispari)

#Ordinare la lista precedente in ordine decrescente.

# r=dispari.reverse()
# print(r)


# l.sort(reverse=True)
# print(l)














l.sort(reverse=True)
print(l)

#Contare quante volte l'elemento "2" appare nella lista precedente.

c= l.count(2)
print(c)