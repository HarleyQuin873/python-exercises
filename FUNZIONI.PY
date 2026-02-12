#Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.
# lista=[1,65,87,9,0,11,43,54,2299,22,33,44,55,66,77,88,99,11,2,3,4,5,6,7,8,9]
# def somma_lista(lista2):
#     somma=0
    
#     for i in lista2:
#         somma += i    
#     return somma


# print("La somma dei numeri della lista è: ", somma_lista(lista))

#Scrivi una funzione che prende una stringa e restituisce la stringa invertita.
# stringa = "Marina"


# def inverti(stringa2):
#     inversa=''
#     n=len(stringa2) - 1
#     while(n>=0):
#         inversa += stringa2[n]
#         n -= 1

#     return inversa

# print("La stringa invertita è: ", inverti(stringa))

#Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.

# lista= ["Marina", "Pugliese", "gatto", "barca", "cucina", "Miele", "Monica", "letto", "PC"]

# def filtro(lista2, lettera):
#     lista3 = []
#     for parola in lista2:
#         if parola[0] ==lettera:
#             lista3.append(parola)
#     return lista3

# print("Lista delle parole che cominciano con: ", filtro(lista, 'b'))


#Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.

# numeri=[1, 12,34,56,78,7,90,9, 65,3]

# def pari(numeri2):
#     l2 = []
#     for elemento in numeri:
#         if elemento %2 == 0:
#             l2.append(elemento)
#     return l2

# print("Lista numeri pari: ", pari(numeri))


#Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola


# lista= ["Marina", "Pugliese", "gatto", "barca", "cucina", "Miele", "Monica", "letto", "PC"]

# def lunghezza(lista2):
#     numeri = []
#     for parola in lista2:
#         l = len(parola)
#         numeri.append(l)
#     return numeri

# print("Lunghezza delle parole della lista:", lunghezza(lista))

#Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo.


# numeri = [1, 12, 34, 56, 78, 7, 90, 9, 65, 3]

# def max_lista(num):
#     massimo = 0
#     for n in num:
#         if n > massimo:
#             massimo = n
#     return massimo

# print("Il valore massimo è: ", max_lista(numeri))

#Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga.

# lista= ["Marina", "Pugliese", "gatto","supercalifragilistichespiralitoso", "barca", "cucina", "Miele", "Monica", "letto", "PC"]

# def parola_max(l1):
#     massima=l1[0]
#     for parola in l1:
#         if len(parola)>len(massima):
#             massima= parola
#     return massima

# print("La parola più lunga è: ", parola_max(lista))


#Scrivi una funzione che prende una lista di numeri e restituisce la media dei numeri.

# numeri = [1, 12, 34, 56, 78, 7, 90, 9, 65, 3]

# def media(l1):
#     somma=0
#     m=0
#     for n in l1:
#         somma += n
#     m = somma / len(l1)

#     return m

# print("La media dei numeri è: ", media(numeri))

#Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole palindrome.

# lista= ["Marina", "Pugliese", "gatto","supercalifragilistichespiralitoso", "barca", "cucina", "Miele", "Monica", "letto", "PC","otto", "anna","alla"]

# def palindrome(l1):
#     p=[]
    
#     n=0
#     for parola in l1:
#         inversa=''
#         n=len(parola) - 1

#         while(n>=0):
#             inversa += parola[n]
#             n -= 1

#         if inversa==parola:
#             p.append(parola)
            
     
#     return p

# print("Lista delle parole palindrome: ", palindrome(lista))

#Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri maggiori di un valore specificato.

numeri = [1, 12, 34, 56, 78, 7, 90, 9, 65, 3]
m=0
def numeri_maggiori_di(l1,m):
    l=[]
    for n in l1:
        if n > m:
            l.append(n)
    return l

print("Lista numeri maggiori di 30: ", numeri_maggiori_di(numeri, 30))



