#Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.
l=("mercedes", "bmw", "porche", "ferrari", "rolls royce")
for elemento in l:
    print(elemento)

#Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.

for numero in range(1,11):
    print(numero)

#Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.
somma=0
l=(1,2,3,4,5,6,7,8,9,10)
for n in l:
    somma = somma + n

print("La somma è:", somma)
#print("Somma: {}".format(somma))

#Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.

for p in range(1,21):
    if p%2==0:
        print(p)

#Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.
s= "Marina è brava, anzi bravissima!!!!!!!!!!!!!!!!"
for c in s:
    print(c)

#Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.

d={
    "nome":"Marina",
    "cognome":"Pugliese",
    "età": 41,
    "indirizzo": "Via *************",
    "città":"*************",
    "titolo": "dottoressa in informatica"
}
for elemento in d:
    print(elemento)

#Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.

for e,v in d.items():
    print(e, ":",v)

#Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista.
l=("pippo", "pluto", "topolino")
for elemento in l:
    for c in elemento:
        print(c)

#Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.
ng=0
s="irugherhgeiurhgerghoerihgèoweifjwqoijwehgeirughreiugheuripqhgewoiufhewoihxrfweoihfewqsoihfcqwiuesghirugphuehfcewiuhfcpioewhtcewiohrctewoisthmreoimhoehqeoighcp,gceirohmweihoehig"
for c in s:
    if c=='g':
        ng += 1
   
print("La lettera g compare ", ng, "volte.")

#Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.
numeri=(324, 654, 67, 456, 56765, 765, 4,4,7,78,89,4,3,6,78,9,65,4,3)
media=0
somma=0
for n in numeri:
    somma+=n

media=somma/len(numeri)
print("La media è: ", media)




