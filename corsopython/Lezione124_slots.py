class Automobile:
    # __slots__=[marca, modello]

    def __init__(self,marca,modello):
        self.marca=marca
        self.modello=modello
       # self.anno=anno
    
mia_auto=Automobile("Toyota", "Yaris")
#mia_auto.anno=2010
print("Marca: ", mia_auto.marca)
print("Modello: ", mia_auto.modello)
#print("Anno: ", mia_auto.anno)
print(mia_auto.__dict__)
#sua_auto=Automobile("Honda", "Civic"
# , "2020"
#)

#print("Anno: ", sua_auto.anno)