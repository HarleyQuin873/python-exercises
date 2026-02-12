class Pianeta:
   
    def __init__(self,nome,risorse):
        self.nome=nome
        self.risorse= risorse

class Astronave:
    
    def __init__(self, capacità_carico=150):
        self.capacità_carico = capacità_carico
        self.carico_attuale = 0
        self.risorse_raccolte = {}


    def astronave_standard(cls): #self, capacità_carico=150):
        return cls(capacità_carico=150)#__init__(self, capacità_carico)

    def capacità_rimanente(self): 
        return self.capacità_carico - self.carico_attuale #diff 

    @staticmethod
    def messaggio_esplorazione(p):
        return print(f"L'astronave sta esplorando il pianteta {p.nome}")

    def __verifica_capacità__(self,massa) -> bool:
        return self.carico_attuale + massa <= self.capacità_carico          
    
    def esplora(self, p):
        self.messaggio_esplorazione(p)
        for chiave,valore in p.risorse.items():
            if self.__verifica_capacità__(valore):
                if valore <= self.capacità_rimanente():
                    if chiave in self.risorse_raccolte:
                        self.risorse_raccolte[chiave] += valore
                    else:
                        self.risorse_raccolte[chiave] = valore
                    self.carico_attuale += valore
                else:
                    print(f"")
            else: 
                print("Impossibile raccogliere ulteriori risorse.")
        print(f"Risorse raccolte: {self.risorse_raccolte}")
        print(f"Carico attuale: {self.carico_attuale}")
        
        
risorse = {"uranio": 5}
Venere = Pianeta("Venere", risorse)
r2 = {"mercurio": 3}
Mercurio = Pianeta("Mercurio", r2)
r3 = {"gas": 1}
Giove = Pianeta("Giove", r3)
 
Nabuccodonosor = Astronave()
Nabuccodonosor.esplora(Venere)
Nabuccodonosor.esplora(Mercurio)
Nabuccodonosor.esplora(Giove)

print(f"Nabuccodonosor.risorse_raccolte: {Nabuccodonosor.risorse_raccolte} ")


