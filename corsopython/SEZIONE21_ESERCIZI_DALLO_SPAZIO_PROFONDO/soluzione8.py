from abc import ABC, abstractmethod


class StatoModulo(ABC):
    @abstractmethod
    def handle_request(self, contesto):
        pass

class StatoAnalisi(StatoModulo):
    def handle_request(self, contesto):
        print(f"{contesto.nome} è in stato di analisi dei dati.")

class StatoRaccoltaDati(StatoModulo):
    def handle_request(self, contesto):
        print(f"{contesto.nome} è in stato di raccolta dati.")

class StatoStandby(StatoModulo):
    def handle_request(self, contesto):
        print(f"{contesto.nome} è in standby.")

class StatoManutenzione(StatoModulo):
    def handle_request(self, contesto):
        print(f"{contesto.nome} è in manutenzione.")

class ModuloScientifico:
    def __init__(self, nome):
        self.nome = nome
        self.stato = StatoStandby()

    def set_state(self, stato):
        self.stato = stato

    def richiesta(self):
        self.stato.handle_request(self)

modulo1 = ModuloScientifico("Nebula")
modulo2 = ModuloScientifico("Galileo")
modulo3 = ModuloScientifico("Celestia")

modulo1.set_state(StatoAnalisi())
modulo2.set_state(StatoRaccoltaDati())
modulo3.set_state(StatoManutenzione())

print("*** Turno 1")
modulo1.richiesta()
modulo2.richiesta()
modulo3.richiesta()

modulo1.set_state(StatoManutenzione())
modulo2.set_state(StatoAnalisi())
modulo3.set_state(StatoRaccoltaDati())

print("*** Turno 2")
modulo1.richiesta()
modulo2.richiesta()
modulo3.richiesta()
