#Data una lista di numeri, crea un iteratore che restituisca solo i numeri pari.

# l=[1,2,3,4,5,6,7,8,9,10]

# class Pari:
#     def __init__(self,numeri):
#         self.numeri=numeri
#         self.index=0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.index < len(self.numeri):
#             if self.numeri[self.index] % 2 == 0:
#                 valore = self.numeri[self.index]
#                 self.index += 1
#                 return valore
#             else:
#                 self.index += 1
#         raise StopIteration

# iteratore_pari = Pari(l)

# for n in iteratore_pari:
#     print(n)

#Data una stringa, crea un iteratore che restituisca ogni carattere della stringa in ordine inverso.

# s="Marina Pugliese"

# class Inversa:
#     def __init__(self, stringa):
#         self.stringa=stringa
#         self.index=len(stringa)-1
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= 0:
#             char = self.stringa[self.index]
#             self.index -= 1
#             return char
#         else:
#             raise StopIteration

# iteratore_inversa = Inversa(s)

# for c in iteratore_inversa:
#     print(c, end='')

#Data una lista di parole, crea un iteratore che restituisca solo le parole che contengono una data lettera

parole=["Marina", "Pugliese", "gatto", "cane", "zucchero", "sale", "Kennedy", "Jack", "Yris"]

class Lettera:
    def __init__(self,lista,carattere):
        self.lista=lista
        self.carattere=carattere
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.lista):
            parola = self.lista[self.index]
            self.index += 1
            if self.carattere in parola:
                return parola
        raise StopIteration
    
iteratore_con_lettera = Lettera(parole,"J")

for c in iteratore_con_lettera:
    print(c)





#Data una lista di numeri, crea un iteratore che restituisca la somma cumulativa dei numeri.

l=[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,987765,4332,222]

# class Somma:
#     def __init__(self,lista):
#         self.lista=lista
#         self.somma=0
#         self.index=0
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.lista):
#             self.somma += self.lista[self.index]
#             self.index += 1
#             return self.somma
#         else:
#             raise StopIteration

# iteratore_numeri=Somma(l)

# for n in iteratore_numeri:
#     print(n)










class Somma_cumulativa:
    def __init__(self,lista):
        self.lista=lista
        self.somma=0
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lista):
            self.somma += self.lista[self.index]
            self.index += 1
            return self.somma
        else:
            raise StopIteration

iteratore_numeri= Somma_cumulativa(l)

for somma in iteratore_numeri:
    print(somma)
