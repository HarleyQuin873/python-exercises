#Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper() 
# per convertirla in maiuscolo in una nuova variabile.

stringa = "ciao mondo"

maiuscolo = stringa.upper()

print(maiuscolo)

#Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() 
# per convertirla in minuscolo in una nuova variabile.

stringa = "Benvenuti a Roma"
minuscolo = stringa.lower()
print(minuscolo)

#Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e
#  utilizzare il metodo split() per dividere la stringa in una lista di parole.

stringa="Il meglio deve ancora venire"
lista= stringa.split()
print(lista)

#Assegnare una stringa "Hello World" ad una variabile "stringa" e 
# utilizzare il metodo replace() per sostituire "World" con "Python".
stringa="Hello World"
a=stringa.replace('World', 'Python')
print(a)

#Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare 
# il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa..

stringa =" Ciao "
s=stringa.strip()
print(s)

#Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.
stringa="abvdsdjgd"
a=stringa[:3]
print(a)

#Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith()
#  per verificare se la stringa inizia con "Py".

stringa="Python"
b=stringa.startswith('Py')
print(b)

#Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo
#  count() per contare il numero di volte in cui la lettera "o" appare nella stringa.
stringa="Ciao mondo"
c=stringa.count('o')
print(c)


#Assegnare una stringa "Ciao mondo" ad una variabile "stringa". Mandare quindi a schermo gli ultimi 
# 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".

stringa="Ciao mondo"
d=stringa[:-5].upper().replace('O','K')
print(d)

#