#esercizio08

from abc import ABC, abstractmethod

class StatoModulo(ABC):

    @abstractmethod
    def handle_request(self):
        pass

class StatoAnalisi(StatoModulo):

    def handle_request(self, modulo):
        print(f"Stato analisi del modulo: {modulo.nome}.")

class StatoRaccoltaDati(StatoModulo):

    def handle_request(self, modulo):
        print(f"Stato Raccolta dati del modulo {modulo.nome}.")

class StatoStandBy(StatoModulo):

    def handle_request(self, modulo):
        print(f"Stato StatoStandBy del modulo {modulo.nome}.")

class StatoManutenzione(StatoModulo):

    def handle_request(self, modulo):
        print(f"Sato StatoManutenzione del modulo {modulo.nome}.")

class ModuloScientifico:

    def __init__(self, nome):
        self.nome=nome
        self.state = StatoStandBy()

    def set_state(self, stato):
        self.state=stato

    def richiesta(self):
        self.state.handle_request(self)

    def __str__(self):
        return f"Il modulo {self.nome} è nel corrente {self.state.__class__.__name__} stato"

    
scudi = ModuloScientifico("Scudi")
Modulo_navigazione =  ModuloScientifico("Modulo_navigazione")
Modulo_difesa = ModuloScientifico("Modulo_difesa")

# print(f"Scudi: {scudi}")
# print(f"Modulo_navigazione: {Modulo_navigazione}")
# print(f"ModuloDifesa: {Modulo_difesa}")

print(scudi)
print(Modulo_navigazione)
print(Modulo_difesa)

scudi.set_state(StatoAnalisi())
Modulo_navigazione.set_state(StatoRaccoltaDati())
Modulo_difesa.set_state(StatoManutenzione())

scudi.richiesta()
Modulo_navigazione.richiesta()
Modulo_difesa.richiesta()

scudi.set_state(StatoManutenzione())
Modulo_navigazione.set_state(StatoAnalisi())
Modulo_difesa.set_state(StatoRaccoltaDati())

scudi.richiesta()
Modulo_navigazione.richiesta()
Modulo_difesa.richiesta()

    