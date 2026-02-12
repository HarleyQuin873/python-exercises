#Creare un set vuoto e assegnarlo a una variabile.

# s = set()
# print(s)

#Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".

s = set([ "mela", "banana", "kiwi","mela"] )
print(s)

#Aggiungere l'elemento "pesca" al set precedente.

s.add("pesca")
print(s)

#Rimuovere l'elemento "mela" dal set precedente.
s.remove("mela")
print(s)

#Verificare se l'elemento "ananas" è presente nel set precedente.

if "ananas"  in s:
    print("L'elemento ananas è presente nel set.")
else:
    print("L'elemento ananas non è presente nel set.")

#Creare un nuovo set contenente gli elementi "banana", "kiwi" e "arancia".
w= set(("banana", "kiwi", "arancia"))
print(w)

#Creare un set contenente i numeri interi da 1 a 5 ricavati da un range().
r= set(range(1,6))
print(r)

#Creare un nuovo set contenente i numeri pari del set precedente.
e=set(x for x in r if x%2==0)

print(e)