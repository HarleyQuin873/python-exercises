class Conto:
    def __init__(self, nome, conto):

        self.nome = nome
        self.conto = conto

class ContoCorrente(Conto):   #la classe  ContoCorrente eredita dalla classe Conto

    __saldo = 0.0

    def __init__(self, nome, conto, importo):
        
        super().__init__(nome,conto)

        self.__saldo = importo
    
    def preleva(self,importo):
        self.__saldo -= importo

    def deposita(self,importo):

        self.__saldo += importo

    def descrizione(self):
        print("Nome: ", self.nome)
        print("Conto corrente: ", str(self.conto))
        print("Saldo: ", str(self.__saldo))

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente,destinazione,importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)



cliente1=ContoCorrente("Marina", 1, 3000000)
cliente2= ContoCorrente("Rosa", 2, 7777)
cliente1.descrizione()
cliente2.descrizione()

print("Bonifico da cliente1 a cliente2")
GestoreContiCorrenti.bonifico(cliente1,cliente2, 3000)

cliente1.descrizione()
cliente2.descrizione()

print("Prelevamento")
cliente1.preleva(300)
cliente2.preleva(500)

cliente1.descrizione()
cliente2.descrizione()

print("Deposito")
cliente1.deposita(2000)
cliente2.deposita(3000)

cliente1.descrizione()
cliente2.descrizione()

print("Saldo di : ", cliente1.nome ,"è: " , cliente1.saldo)

print("Saldo di : ", cliente2.nome ,"è: " , cliente2.saldo)





        


    