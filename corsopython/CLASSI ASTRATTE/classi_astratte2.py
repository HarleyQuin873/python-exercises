from abc import ABC, abstractmethod

class Personaggio(ABC):
    def __init__(self,nome):
        self.nome=nome
    
    @abstractmethod
    def attacca(self):
        pass

class Guerriero(Personaggio):
    def attacca(self):
        return f"{self.nome} sferza un potente colpo di spada"
    # pass

class Mago(Personaggio):
    def attacca(self):
        return f"{self.nome} lancia un incantesimo magico"

class Ladro(Personaggio):
    def attacca(self):
        return f"{self.nome} attacca furtivamente con un pugnale"

if __name__ == "__main__":
    aragorn = Guerriero("Aragon")
    gandalf = Mago("Gandalf")
    bilbo = Ladro("Bilbo")

    print(aragorn.attacca())
    print(gandalf.attacca())
    print(bilbo.attacca())





