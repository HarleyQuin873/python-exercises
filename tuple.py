#Creare una tupla vuota e assegnarla a una variabile.
tupla=()
print(tupla)

#Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".
t=("mela", "banana", "kiwi")
print(t)

#Accedere all'elemento "banana" della tupla precedente.

secondo=t[1]
print(secondo)

#Creare una nuova tupla che contenga solo i primi due elementi della tupla precedente.

t2=(t[0], t[1])
print(t2)

#Verificare se l'elemento "ananas" è presente nella tupla precedente.

if "ananas" in t2:
    print("L'elemento ananas è presente nella tupla.")
else:
    print("L'elemento ananas non è presente nella tupla.")

#Creare una nuova tupla concatenando la tupla precedente con la tupla ("pesca", "arancia").

t3=t + ("pesca", "arancia")
print(t3)

#Verificare la lunghezza della tupla precedente.

lunghezza= len(t3)
print(lunghezza)

#Creare una tupla contenente i numeri interi da 1 a 5.
numeri=(1,2,3,4,5)
print(numeri)

#Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.
q=(1**2,2**2,3**2,4**2,5**2)
print(q)

#Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.

c=t3.count("mela")
print(c)

#