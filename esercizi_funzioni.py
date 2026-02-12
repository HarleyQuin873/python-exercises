#Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.
lista=(1,2,3,4,55,68,89,0,987)
def somma_lista(lista2):
    somma = 0
    for elemento in lista2:
        somma+= elemento
    return somma

print(somma_lista(lista))

#Scrivi una funzione che prende una stringa e restituisce la stringa invertita.

def inverti(stringa):
    inversa = ''
    indice = len(stringa) -1
    while indice > 0:
        inversa += stringa[indice]
        indice -= 1
    return inversa

print(inverti("dfbgdfkjbgdkfbg"))

#Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.
lista = ("io", "tu", "tiziana", 'marika', "milly", "carla", "zio", "pino")
def filtro(lista2, lettera):
    ll = []
    for parola in lista2:
        if parola[0] == lettera:
            ll.append(parola)
    return ll

print(filtro(lista, 't'))

#Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.
lista = (34,7667,9,5,4,22,1)

def num_pari(lista3):
    l4 = []
    for e in lista3:
        if e % 2 == 0:
            l4.append(e)
    return l4
print(num_pari(lista))

#Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.
l=("pae", "mio", "tuo", "suo", "egli", "noi", "voi", "essi")
def len_word(l1):
    l2 = []
    for p in l1:
        nn = len(p)
        l2.append(nn)
    return l2
print(len_word(l))

#Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo.
l = (1,2,3,4,5,6,7,8,9,987,654,4323,211,0,88,77,66,55,44,22,11)

def vmax(l1):
    massimo = l1[0]
    for nn in l1:
        if nn > massimo:
            massimo = nn
    return massimo
print(vmax(l)) 

#Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga.
l=("uno", "duer", "treee", "quattrooo", "a", "dfgdfihgifdugdfg")
def wordmax(l1):
    maxx = len(l1[0])
    for w in l1:
        if len(w) > maxx:
            maxx = len(w)
    return maxx
print(wordmax(l))

#Scrivi una funzione che prende una lista di numeri e restituisce la media dei numeri.
l = (1,2,3,4,5,6,7,8,9,987,654,4323,211,0,88,77,66,55,44,22,11)
def media(l1):
    med = 0
    somma = 0
    for n1 in l1:
        somma += n1
    med = somma/ len(l1)
    return med
print(media(l))

#Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole palindrome.
l=("anna", "acca", "zio", "quadro")
def palindrome(l1):
    p = []
    for w in l1:
        if w == w[::-1]:
            p.append(w)
            # Per prima cosa abbiamo calcolato il valore inverso della parola originale con [::-1] come indice della lista.
            #if parola == parola[::-1]:
           # risultato.append(parola)
            
    return p

print(palindrome(l))

#Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri maggiori di un valore specificato.
l = (1,2,3,4,5,6,7,8,9,987,654,4323,211,0,88,77,66,55,44,22,11)
n=50
def maxn(l1, n2):
    l2 = []
    for m in l1:
        if m > n2:
            l2.append(m)
    return l2

print(maxn(l,n))
    
