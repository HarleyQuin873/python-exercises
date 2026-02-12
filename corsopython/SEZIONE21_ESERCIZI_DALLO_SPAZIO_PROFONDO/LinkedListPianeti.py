#esercizio04
class Pianeta:
    def __init__(self,nome):
        self.nome=nome
        self.successivo=None
    
class LinkedListPianeti:

    def __init__(self):
        self.testa=None

    def aggiungi_pianeta(self, p:Pianeta):
        nuovo_pianeta = Pianeta(p.nome)
        nuovo_pianeta.successivo= self.testa
        self.testa= nuovo_pianeta
        # self.add(p)
        # print(f"Pianeta {p} aggiunto.")
    
    def visualizza_pianeti(self):
        corrente= self.testa
        while corrente:
            print(corrente.nome, end="->")
            corrente = corrente.successivo
        print("None")
         # for i in self:
        #     print(i.nome)

pianeta1 = Pianeta("Venere")
pianeta2 = Pianeta("Sole")
pianeta3 = Pianeta("Luna")
pianeta4 = Pianeta("Marte")
pianeta5 = Pianeta("Giove")
pianeta6 = Pianeta("Saturno")
pianeta7 = Pianeta("Nettuno")
pianeta8 = Pianeta("Urano")
pianeta9 = Pianeta("Mercurio")
pianeta10 = Pianeta("Plutone")
pianeta11 = Pianeta("Eris")
pianeta12 = Pianeta("Haumea")
pianeta13 = Pianeta("Makemake")
pianeta14 = Pianeta("Ceres")
pianeta15 = Pianeta("Terra")

lp = LinkedListPianeti()

lp.aggiungi_pianeta(pianeta1)
lp.aggiungi_pianeta(pianeta10)
lp.aggiungi_pianeta(pianeta11)
lp.aggiungi_pianeta(pianeta12)
lp.aggiungi_pianeta(pianeta13)
lp.aggiungi_pianeta(pianeta14)
lp.aggiungi_pianeta(pianeta15)

lp.aggiungi_pianeta(pianeta2)
lp.aggiungi_pianeta(pianeta3)
lp.aggiungi_pianeta(pianeta4)
lp.aggiungi_pianeta(pianeta5)
lp.aggiungi_pianeta(pianeta6)
lp.aggiungi_pianeta(pianeta7)
lp.aggiungi_pianeta(pianeta8)
lp.aggiungi_pianeta(pianeta9)

lp.visualizza_pianeti()