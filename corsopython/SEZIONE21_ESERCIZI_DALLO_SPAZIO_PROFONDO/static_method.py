#esercizio 02
class Pianeta:
    def __init__(self, nome,risorse):
        self.nome=nome
        self.risorse=risorse

class Astronave:

    def __init__(self, capacità_carico=150):
        self.capacità_carico=capacità_carico
        self.carico_attuale=0
        self.risorse_raccolte={}

    @classmethod
    def astronave_standard(cls):
        return cls(capacità_carico=150) #I metodi di classe in Python servono a operare sulla classe stessa, piuttosto che su un'istanza specifica di quella classe. Questi metodi sono definiti con il decoratore @classmethod e prendono come primo parametro cls (anziché self che si usa nei metodi di istanza). In pratica, i metodi di classe hanno accesso alla classe e possono modificarne attributi o creare nuove istanze della classe stessa.In questo modo, il metodo astronave_standard diventa un metodo di classe e può utilizzare cls per creare una nuova istanza di Astronave.

    def capacità_rimanente(self):
        return self.capacità_carico - self.carico_attuale

    @staticmethod
    def messaggio_esplorazione(p):
        return f"L'astronave sta esplorando il pianeta {p.nome}"

    def __verifica_capacità__(self, massa) -> bool:

        #__ metodo privato
        return self.carico_attuale + massa <= self.capacità_carico

    def esplora(self,p):
        self.messaggio_esplorazione(p)
        for chiave,valore in  p.risorse.items():
            if self.__verifica_capacità__(valore):
                if valore <= self.capacità_rimanente():
                    if chiave in self.risorse_raccolte:
                        self.risorse_raccolte[chiave] +=valore
                    else:
                        self.risorse_raccolte[chiave]= valore
                    self.carico_attuale += valore
                else:
                    print(f"")
            else:
                print("Impossibile raccogliere ulteriori risorse")
        print(f"Risorse raccolte: {self.risorse_raccolte}")
        print(f"Carico attuale: {self.carico_attuale}")

risorse= {"uranio" : 5}
Venere= Pianeta("Venere", risorse)
r2={"mercurio": 3}
Mercurio = Pianeta("Mercurio", r2)
r3= {"gas": 1}
Giove = Pianeta("Giove", r3)

Nabuccodonosor = Astronave()
Nabuccodonosor.esplora(Venere)
Nabuccodonosor.esplora(Mercurio)
Nabuccodonosor.esplora(Giove)

print(f"Nabuccodonosor.risorse_raccolte: {Nabuccodonosor.risorse_raccolte}")