#Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.
# l=(1,2,3,"pippo", "pluto", "topolino")

# for i in l:
#     print(i)

#Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.
# numeri=(0,1,2,3,4,5,6,7,8,9)
# for n in numeri:
#     print(n)


# for r in range(10):
#     print(r)

#Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.
# lista=(0,1,2,3,4,5,6,7,8,9)
# somma=0
# for s in lista:
#     somma = somma + s
    
# print("La somma è: ", somma)


#Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.

# for i in range(0,20):
#     if (i%2 == 0):
#         print(i)

#Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.
# s="Marina è brava."
# for a in s:
#     print(a)


#Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
# dictionary = {
#     "nome":"Marina",
#     "cognome":"Pugliese"
# }
# for key in dictionary:
#     print(key)

#Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.
# d={
#      "nome":"Marina",
#      "cognome":"Pugliese",
#      "hobby":"ballare"
# }

# for k,v in d.items():
#     print(k, ":", v)


#Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista.

# lista=("Marina", "Pugliese")

# for parola in lista:
#     for lettera in parola:
#         print(lettera)

#Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.

# n=0;
# lettera="g"
# s="rughariugaeirugairugaiudrgabdfbgdfgbadfgbadfhgbdfbg"

# for i in s:
#     if (i == lettera):
#         n += 1
    
# print("La lettera ", lettera, "compare " , n," volte.")

#Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.

lista = (1, 55, 88, 99, 0, 4, 2345, 9876)
somma = 0
media = 0
for i in lista:
    somma = somma + i
media = somma / len(lista)

print("La media è: ", media)
