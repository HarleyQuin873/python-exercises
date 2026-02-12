#Data una lista di numeri, crea un iteratore che restituisca solo i numeri pari.

l = (1,2,3,44,55,66)

class Pari:
    def __init__(self, numeri):
        self.numeri = numeri
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numeri):
            if self.numeri[self.index] % 2 == 0:
                valore = self.numeri[self.index]
                self.index += 1
                return valore
            else:
                self.index += 1
        raise StopIteration

iteratore_pari = Pari(l)

for numero in iteratore_pari:
    print(numero)


#Data una stringa, crea un iteratore che restituisca ogni carattere della stringa in ordine inverso.

stringaa = "rjkgbkrjgbgbrgbgbgbdfbg"

class Inversa:
    def __init__(self,stringa):
        self.stringa = stringa
        self.index = len(stringa)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.stringa[self.index]
        else:
            raise StopIteration
    

iteratore_inversa = Inversa(stringaa)

for carattere in iteratore_inversa:
    print(carattere)
    

#Data una lista di parole, crea un iteratore che restituisca solo le parole che contengono una data lettera

parolee=("ciao", "mondo", "giuggiola", "gabbiano", "giocattolo", "giovane", "sabbia", "mare", "mojito")
letteraa = 'g'
class Restituisci_lettera:

    def __init__(self, lista_parole, lettera):
        self.parole =lista_parole
        self.lettera = lettera
        self.index = 0

    def __iter__(self):
        return self
    
    # def __next__(self):
    #    # li = []
    #     for parola in self.parole:
    #         if self.lettera in parola:
    #             return parola
    #     raise StopIteration
    
    def __next__(self):
        while self.index < len(self.parole):
            if self.lettera in self.parole[self.index]:
                valore = self.parole[self.index]
                self.index += 1
                return valore
            else:
                self.index += 1
        raise StopIteration
    
iteratore_lettera = Restituisci_lettera(parolee, letteraa)
#Restituisci_lettera(parolee, 'g')

for parola in iteratore_lettera:
    print(parola)


# parolee = ["casa", "cane", "gatto", "auto", "treno", "bicicletta"]
# letteraa = "a"

# class ConLettera:
#     def __init__(self, parole, lettera):
#         self.parole = parole
#         self.lettera = lettera
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.index < len(self.parole):
#             if self.lettera in self.parole[self.index]:
#                 valore = self.parole[self.index]
#                 self.index += 1
#                 return valore
#             else:
#                 self.index += 1
#         raise StopIteration

# iteratore_con_lettera = ConLettera(parolee, letteraa)

# for parola in iteratore_con_lettera:
#     print(parola)

#Data una lista di numeri, crea un iteratore che restituisca la somma cumulativa dei numeri.
l=(123,456,789,90,987,76,545,43,22,21,11,4)
class Somma_cumulativa():
    def __init__(self, numeri):
        self.lista_numeri = numeri
        self.index = 0
        self.somma=0

    def __iter__(self):
        return self
    
    def __next__(self):    
        if self.index < len(self.lista_numeri):
            self.somma += self.lista_numeri[self.index]
            self.index += 1
            return self.somma
        else:
            raise StopIteration
        
    
iteratore_numeri = Somma_cumulativa(l)

for somma in iteratore_numeri:
    print(somma)

