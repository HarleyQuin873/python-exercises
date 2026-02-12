import math

class Astronave:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def muovi_a(self, dest_x, dest_y):
        self.x = dest_x
        self.y = dest_y
        print(f"L'astronave si è mossa alle coordinate ({self.x}, {self.y}).")
    
    def distanza_da(self, dest_x, dest_y):
        return math.sqrt((dest_x - self.x) ** 2 + (dest_y - self.y) ** 2)

# Esempio di utilizzo:
epsilon = Astronave(0, 0)  # l'astronave parte dall'origine

# Muove l'astronave alle coordinate (5, 5)
epsilon.muovi_a(5, 5)

# Calcola e stampa la distanza dall'origine
distanza = epsilon.distanza_da(0, 0)
print(f"L'astronave è a {distanza} unità di distanza dall'origine.")
