#Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper() 
# per convertirla in maiuscolo in una nuova variabile.

s='Ciao mondo'
s2=s.upper()
print(s,s2)

#Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() 
# per convertirla in minuscolo in una nuova variabile.

stringa="Benvenuti a Roma"
s3=stringa.lower()
print(stringa, s3)

#Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e
#  utilizzare il metodo split() per dividere la stringa in una lista di parole.

a="Il meglio deve ancora venire"
b=a.split()
print(a)
print(b)

#Assegnare una stringa "Hello World" ad una variabile "stringa" e 
# utilizzare il metodo replace() per sostituire "World" con "Python".

c="Hello World"
d=c.replace("World", "Python")
print(c)
print(d)

#Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare 
# il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa..

s5="   Ciao   "
s6=s5.strip()
print(s5)
print(s6)

#Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.

ss="abcdefg"
cc=ss[:3]
print(ss)
print(cc)

#Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith()
#  per verificare se la stringa inizia con "Py".

pp="Python"
ppp=pp.startswith("Py")
print(pp)
print(ppp)

#Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo
#  count() per contare il numero di volte in cui la lettera "o" appare nella stringa.

q="Ciao mondo"
g=q.count("o")
print(q)
print(g)

#Assegnare una stringa "Ciao mondo" ad una variabile "stringa". Mandare quindi a schermo gli ultimi 
# 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".

print(q[5:].upper().replace("O","k"))