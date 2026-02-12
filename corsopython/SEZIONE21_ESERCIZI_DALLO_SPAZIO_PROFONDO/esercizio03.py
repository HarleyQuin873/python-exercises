# def singleton(cls):
#     istanze = {}

#     def get_instance(*args, **kwargs):
#         if cls not in istanze:
#             istanze[cls] = cls(*args, **kwargs)
#         return istanze[cls]

#     return get_instance

# @singleton
class ComputerCentrale:
    _istanza = None
    # stato = ""
    # motori = ""

    # @classmethod
    # def _astronave_standard(cls):
    #     return cls()

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
        
    
istanza1 = ComputerCentrale()
istanza2 = ComputerCentrale()


print(istanza1 == istanza2)

print(istanza1.statoAstronave())
istanza1.avviaMotori()
print(istanza2.statoAstronave())
istanza2.spegniMotori()
print(istanza1.statoAstronave())


# print(computer1.statoAstronave())
# computer1.avviaMotori()
# print(computer2.statoAstronave())
# computer2.spegniMotori()
# print(computer1.statoAstronave())

    
   

