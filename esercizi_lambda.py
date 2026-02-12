#Scrivi una lambda function che prenda una lista di parole e restituisca una lista contenente 
#solo le parole che iniziano con la lettera "a".
lista = ("io", "tu","albero" ,"egli","aquilone", "noi", "voi", "essi", "anna")
parolea = lambda lista : [x for x in lista if x.startswith("a") ]
print(parolea(lista))


#Scrivi una lambda function che prenda due numeri e restituisca la somma dei loro quadrati.

somma_quadrati = lambda x,y : x**2 + y**2
print(somma_quadrati(3,4))

#Scrivi una lambda function che prenda una stringa e restituisca True se la stringa 
# è palindroma, altrimenti False.

boolean = lambda s : s == s[::-1]
print(boolean("iufgbdifugdifughdfiu"))

#Scrivi una lambda function che prenda una
#  lista di parole e restituisca la lunghezza media delle parole nella lista.

media = lambda l : sum(len(x) for x in l) / len(l)
# [for x in l: 
#                     s+=len(x)
#                     m =s/len(l)
#                     return m]
print(media(lista))

#Scrivi una lambda function che prenda una lista di numeri e restituisca la somma solo dei numeri pari.
l=(1,2,3,4,5,6,7,8,9,10)
s= lambda l : sum(x for x in l if x % 2 == 0)
print(s(l))

#Scrivi una lambda function che prenda una lista di dizionari e restituisca una
#  lista di tutte le chiavi dei dizionari.

lista_dizionari = ({
    "nome": "Marina",
    "cognome": "Pugliese"
},
{ "targa":"ghduighd",
 "modello": "ferrari"})
chiavi = lambda lista : [chiave for dizionario in lista for chiave in dizionario.keys()]
#lista_dizionari.keys
print(chiavi(lista_dizionari))

#Scrivi una lambda function che prenda una lista di 
# numeri e restituisca una lista di tutti i numeri maggiori di 10.

numeri = (432,768,1,0,9,8,7,6,6,45,76,23,56,99,887)
l = lambda n : [x for x in n if x > 10]
print(l(numeri))

#Scrivi una lambda function che prenda una lista di tuple e 
# restituisca una lista di tuple ordinate per il secondo elemento di ciascuna tupla.

lista_tuple = ( ("fd", "skjrb", "gbdgb"),("frt", "gre","fdgdsg"),("dfdsf", "gdfgdsf","gdfgd"))
d = lambda lt : sorted(lt, key=lambda tupla : tupla[1])
#[lt.sort()]
print(d(lista_tuple))
