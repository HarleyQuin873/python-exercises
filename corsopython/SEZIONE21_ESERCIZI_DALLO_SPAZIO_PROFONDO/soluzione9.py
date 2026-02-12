from abc import ABC, abstractmethod

class ComponenteAstronave(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def operazione(self):
        pass
    def aggiungi(self, componente):
        pass
    def rimuovi(self, componente):
        pass
    def ottieniFiglio(self, index):
        pass

class Sistema(ComponenteAstronave):
    def operazione(self):
        print(f"Sistema {self.nome} in operazione.")

class ModuloComplesso(ComponenteAstronave):
    def __init__(self, nome):
        super().__init__(nome)
        self._componenti = []
    def operazione(self):
        print(f"Modulo Complesso {self.nome} in operazione:")
        for componente in self._componenti:
            componente.operazione()
    def aggiungi(self, componente):
        self._componenti.append(componente)
    def rimuovi(self, componente):
        self._componenti.remove(componente)
    def ottieniFiglio(self, index):
        if index < 0 or index >= len(self._componenti):
            return None
        return self._componenti[index]

# Creazione dei singoli sistemi
sistema_navigazione = Sistema("Navigazione")
sistema_difesa = Sistema("Difesa")
sistema_ricerca = Sistema("Ricerca Scientifica")

# Creazione di un modulo complesso
modulo_comando = ModuloComplesso("Modulo Comando")
modulo_comando.aggiungi(sistema_navigazione)
modulo_comando.aggiungi(sistema_difesa)

# Creazione di un altro modulo complesso
modulo_scienza = ModuloComplesso("Modulo Scienza")
modulo_scienza.aggiungi(sistema_ricerca)

# Creazione di un modulo complesso principale
astronave_andromeda = ModuloComplesso("Astronave Andromeda")
astronave_andromeda.aggiungi(modulo_comando)
astronave_andromeda.aggiungi(modulo_scienza)

# Test dell'implementazione
astronave_andromeda.operazione()
