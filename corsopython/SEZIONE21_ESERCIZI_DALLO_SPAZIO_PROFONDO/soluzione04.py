class Pianeta:
    def __init__(self, nome):
        self.nome = nome
        self.successivo = None

class LinkedListPianeti:
    def __init__(self):
        self.testa = None

    def aggiungi_pianeta(self, nome_pianeta):
        nuovo_pianeta = Pianeta(nome_pianeta)
        if self.testa is None:
            self.testa = nuovo_pianeta
            return
        ultimo_pianeta = self.testa
        while ultimo_pianeta.successivo:
            ultimo_pianeta = ultimo_pianeta.successivo
        ultimo_pianeta.successivo = nuovo_pianeta

    def visualizza_pianeti(self):
        pianeta_corrente = self.testa
        while pianeta_corrente:
            print(pianeta_corrente.nome, end=" -> ")
            pianeta_corrente = pianeta_corrente.successivo
        print("Fine lista")


lista_pianeti = LinkedListPianeti()

lista_pianeti.aggiungi_pianeta("Zyphoria")
lista_pianeti.aggiungi_pianeta("Vestralis")
lista_pianeti.aggiungi_pianeta("Narquion")

lista_pianeti.visualizza_pianeti()
