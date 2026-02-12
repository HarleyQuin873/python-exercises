from abc import ABC, abstractmethod

class StatoModulo(ABC):
    
    @abstractmethod
    def handle_request(self):
        pass

    

class StatoAnalisi(StatoModulo):
     
    def handle_request(self, modulo):
        print(f"Stato StatoAnalisi del modulo {modulo.nome}")



class StatoRaccoltaDati(StatoModulo):

    def handle_request(self,modulo):
        print(f"Stato StatoRaccoltaDati del modulo {modulo.nome}")

class StatoStandBy(StatoModulo):

    def handle_request(self,modulo):
        print(f"Stato StatoStandBy del modulo {modulo.nome}")

    
class StatoManutenzione(StatoModulo):

    def handle_request(self,modulo):
        print(f"Stato StatoManutenzione del modulo {modulo.nome}")

class ModuloScientifico:

    def __init__(self,nome):
        self.nome = nome
        self.state = StatoStandBy()

    def set_state(self,stato):
        self.state = stato

    
    def richiesta(self):
        self.state.handle_request(self)

    def __str__(self):
        return f'Il modulo {self.nome} è nel corrente {self.state.__class__.__name__} stato.'


scudi = ModuloScientifico("Scudi")
ModuloNavigazione = ModuloScientifico("Modulo_navigazione")
ModuloDifesa = ModuloScientifico("Modulo_difesa")

print(scudi)
print(ModuloNavigazione)
print(ModuloDifesa)

scudi.set_state(StatoAnalisi())
ModuloNavigazione.set_state(StatoRaccoltaDati())
ModuloDifesa.set_state(StatoManutenzione())

scudi.richiesta()
ModuloNavigazione.richiesta()
ModuloDifesa.richiesta()

scudi.set_state(StatoManutenzione())
ModuloNavigazione.set_state(StatoAnalisi())
ModuloDifesa.set_state(StatoRaccoltaDati())

scudi.richiesta()
ModuloNavigazione.richiesta()
ModuloDifesa.richiesta()


    


