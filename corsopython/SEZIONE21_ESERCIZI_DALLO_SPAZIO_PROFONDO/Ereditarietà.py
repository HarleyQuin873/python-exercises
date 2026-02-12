#esercizio10
from abc import ABC, abstractmethod

class ModuloSpaziale(ABC):

    def __init__(self, nome:str, tipo:str, funzione:str):
        self.nome = nome
        self.tipo = tipo
        self.funzione = funzione

    def __str__(self):
        return f"{self.nome} ({self.tipo}): {self.funzione}"

class ModuloEsplorazione(ModuloSpaziale):

    def __init__(self, nome, tipo, funzione):
        super().__init__(nome, tipo, funzione)

class ModuloDifesa(ModuloSpaziale):

    def __init__(solf, nome, tipo, funzione):
        super().__init__(nome, tipo, funzione)

class ModuloRicerca(ModuloSpaziale):

    def __init__(self, nome, tipo, funzione):
        super().__init__(nome, tipo, funzione)

class Creator(ABC):

    @abstractmethod
    def crea_modulo(self, tipo_modulo:str):
        pass

    
class InvalidModuleError(Exception):
    pass

class FactoryModuliSpaziali(Creator):

    def crea_modulo(self, tipo_modulo) ->ModuloSpaziale:
        moduli_validi = ["esplorativo", "difesa", "scientifico"]
        modulo = None

        if tipo_modulo == "esplorativo":
            modulo = ModuloEsplorazione("Modulo Esplorazione", "esplorativo", "esplorazione") 
            return modulo
        elif tipo_modulo == "difesa":
            modulo = ModuloDifesa("Modulo di difesa", "difesa", "difesa")
            return modulo
        elif tipo_modulo == "scientifico":
            modulo = ModuloRicerca("Modulo di ricerca", "ricerca", "ricerca")
            return modulo
        else:
            if tipo_modulo not in moduli_validi:
                raise InvalidModuleError(f"Tipo modulo non valido: {tipo_modulo}")

try:
    f =  FactoryModuliSpaziali()
    e =  f.crea_modulo("esplorativo")
    print(f"Modulo creato: {e.nome}")
    d = f.crea_modulo("difesa")
    print(f"Modulo creato: {d.nome}")
    r = f.crea_modulo("scientifico")
    print(f"Modulo creato: {r.nome}")
    i= f.crea_modulo("prova_errore")
except InvalidModuleError as error:
    print(error)