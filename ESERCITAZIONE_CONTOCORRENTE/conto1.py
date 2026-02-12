class Conto:
    

    def __init__(self,nome,conto):
        self.nome = nome
        self.conto = conto


class ContoCorrente(Conto):
    __saldo = 0.0

    def __init__(self, nome, conto, importo):
       super().__init__(nome,conto)
    
       self.__saldo = importo
    
    def preleva(self,importo):
        self.__saldo = self.__saldo - importo
    
    def deposita(self,importo):
        self.__saldo = self.__saldo + importo
    
    def descrizione(self):
        print("Nome:" + self.nome)
        print("Conto corrente: " + str(self.conto))
        print("Saldo: "  + str(self.__saldo))

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter 
    def saldo(self,importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)
   


cliente1 = ContoCorrente("Marina", 1, 3000000)
cliente2 = ContoCorrente("Rosa", 2, 777777777)
cliente1.descrizione()

cliente2.descrizione()

print("bonifico da cliente1 a cliente2: ")
GestoreContiCorrenti.bonifico(cliente1,cliente2,3000)
cliente1.descrizione()

cliente2.descrizione()

print("Prelevamento")
cliente1.preleva(1000)
cliente2.preleva(2000)

cliente1.descrizione()
cliente2.descrizione()

print("Deposito")
cliente1.deposita(888)
cliente2.deposita(999)

cliente1.descrizione()
cliente2.descrizione()

print(cliente1.saldo)

cliente1.saldo = 10000

print(cliente1.saldo)

c3 = ContoCorrente("Luke Perry", 3, 90000)

c3.descrizione()
c3.preleva(23)
c3.descrizione()
c3.deposita(42)
c3.descrizione()





