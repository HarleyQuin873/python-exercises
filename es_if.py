#Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo".

# def positivo_negativo():
#     n=int(input("Inserisci un numero:"))

#     if n > 0:
#         print("Il numero è positivo.")
#     else:
#         print("Il numero è negativo.")
   
# positivo_negativo()

##Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore" se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, altrimenti stampa "I numeri sono uguali".

# n=int(input("Inserisci un numero:"))
# m=int(input("Inserisci un altro numero:"))

# if(n>m):
#     print("Il primo numero è maggiore")
# elif (m>n):
#     print("Il secondo numero è maggiore")
# else:
#     print("I due numero sono uguali.")

#Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota, altrimenti stampa "La stringa non è vuota".

# s=str(input("Inserisci una stringa:"))
# if(s==''):
#     print("La stringa è vuota")
# else:
#     print("La stringa non è vuota")

#Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari, altrimenti stampa "Il numero è dispari".

# n=int(input("Inserisci un numero: "))
# if(n % 2 == 0):
#     print("Il numero è pari")
# else:
#     print("Il numero non è pari")

#Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".

# s=str(input("Inserire una lettera: "))

# if( s in 'aeiouAEIOU'):
#     print("La lettera è una vocale.")
# else:
#     print("La lettera non è una vocale.")

#Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10" se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".

# n=int(input("Inserisci un numero:"))
# if(n in range(1,10)):
#     print("Il numero è compreso fra 1 e 10.")
# else:
#     print("Il numero non è compreso fra 1 e 10")

#Scrivere un programma che chieda all'utente di inserire un numero intero. Se il numero è maggiore di 10, stampare "Il numero è maggiore di 10". Se il numero è uguale a 10, stampare "Il numero è uguale a 10". Se il numero è minore di 10, stampare "Il numero è minore di 10".

# n=int(input("Inserisci un numero intero:"))
# if(n > 10):
#     print("Il numero è maggiore di 10.")
# elif(n==10):
#     print("Il numero è uguale a 10.")
# else:
#     print("Il numero è minore di 10.")

#Scrivere un programma che chieda all'utente di inserire un carattere. Se il carattere è una vocale (a, e, i, o, u), stampare "Il carattere inserito è una vocale". Se il carattere è una consonante isAlpha(), stampare "Il carattere inserito è una consonante". Se il carattere non è una lettera, stampare "Il carattere inserito non è una lettera".

# s=str(input("Inserire un carattere: "))
# if( s in 'aeiouAEIOU'):
#     print("Il carattere è una vocale.")
# elif( s.isalpha()):
#     print("Il carattere inserito è una consonante.")
# else:
#     print("Il carattere inserito non è una lettera.")

#Scrivere un programma che chieda all'utente di inserire tre numeri interi. Il programma deve verificare se i tre numeri formano un triangolo rettangolo. Se i tre numeri formano un triangolo rettangolo, stampare "I tre numeri formano un triangolo rettangolo". Altrimenti, stampare "I tre numeri non formano un triangolo rettangolo".

a=int(input("Inserisci il primo lato:"))
b=int(input("Inserisci il secondo lato:"))
c=int(input("Inserisci il terzo lato:"))
if(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 ):
    print("I tre numeri rappresentano tre lati di un triangolo rettangolo.")
else:
    print("I tre numeri non rappresentano i lati di un triangolo rettangolo")


