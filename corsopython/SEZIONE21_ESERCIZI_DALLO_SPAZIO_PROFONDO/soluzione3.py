class ComputerCentrale:
    _istanza = None

    def __new__(cls):
        if cls._istanza is None:
            cls._istanza = super().__new__(cls)
            cls._istanza.stato = "In attesa"
            cls._istanza.motori = "Spenti"
        return cls._istanza

    
    def statoAstronave(self):
        return f"Stato Andromeda: {self.stato}, Motori: {self.motori}"

    def avviaMotori(self):
        self.motori = "Accesi"
        self.stato = "In movimento"

    def spegniMotori(self):
        self.motori = "Spenti"
        self.stato = "In attesa"


# Test del Singleton:
computer1 = ComputerCentrale()
computer2 = ComputerCentrale()

print(computer1 == computer2)

print(computer1.statoAstronave())
computer1.avviaMotori()
print(computer2.statoAstronave())
computer2.spegniMotori()
print(computer1.statoAstronave())

