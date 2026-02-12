import random

#Stampare i numeri interi da 1 a 10 usando un loop while.
# i=0
# while(i<11):
#     print(i)
#     i += 1


#Calcolare la somma dei primi n numeri interi positivi usando un loop while. L'utente deve inserire il valore di n.

# print("Inserire un numero n positivo:")
# somma=0
# i=0
# n = int(input("Inserire un numero n positivo:"))
# while(i<=n):
#     somma += i
#     i += 1

# print("La somma dei primi ", n, " numeri positivi è: ",somma)

#Stampare i numeri pari da 2 a 10 usando un loop while.
# i=0
# while(i<11):
#     if(i%2 == 0):
#         print(i)
#     i += 1

#Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10. Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.

# nrandom = random.randint(1,10)

# trovato=False

# #
# while(trovato == False):
#     n=int(input("Indovinare un numero tra 1 e 10:"))
#     if (n == nrandom):
#         trovato=True
#         print("Indovinato!")
#     else:
#         trovato=False
#         print("Sbagliato! Ritenta")

#Chiedere all'utente di inserire una stringa. Stampare la stringa al contrario usando un loop while.

# stringa=str(input("Inserire una stringa: "))
# i= len(stringa) -1
# while(i >= 0):
#     print(stringa[i], end="")
#     i -= 1













#Chiedere all'utente di inserire una stringa. Stampare la stringa al contrario usando un loop while.

# stringa=str(input("Inserire una stringa:"))

# i=len(stringa) -1

# while(i >= 0):
#     print(stringa[i], end="")
#     i -= 1


    











# stringa=str(input("Inserire una stringa:"))
# i=len(stringa)-1

# while(i >= 0):
#     print(stringa[i], end="")
#     i -= 1


#Stampare i numeri da 10 a 1 usando un loop while.

# i=10

# while(i>0):
#     print(i)
#     i -=1


#Calcolare il fattoriale di un numero intero positivo n usando un loop while.

# n=int(input("Inserire un numero intero positivo:"))

# fattoriale=1
# i=1
# while(i <= n):
#     fattoriale *= i
#     i += 1

# print("Il fattoriale di ", n, "è:", fattoriale)

#Calcolare il fattoriale di un numero intero positivo n usando un loop while.

# n=int(input("Inserire un numero intero positivo:"))

# fact=1
# i=1
# while(i <= n):
#     fact *= i
#     i +=1
# print("Il fattoriale di ", n, "è: ", fact)



#Chiedere all'utente di inserire una lista di numeri interi. Stampare la somma di tutti i numeri usando un loop while.

# lista= []

# n=int(input("Quanti numeri vuoi inserire:"))
# # while()
# #     lista[i]=
# i=0
# somma=0
# while(i<n):
#     num=int(input("Inserire numero:"))
#     lista.append(num)
#     somma+=lista[i]
#     i+=1
# print("La somma di tutti i numeri è:" , somma)

#Chiedere all'utente di inserire una stringa. Stampare solo le consonanti della stringa usando un loop while.

stringa=str(input("Inserire una stringa:"))
i=0
i = len(stringa) -1
while(i>=0):
    if(stringa[i] not in 'aeiouAEIOU'):
        print(stringa[i], end="")
    i-=1
