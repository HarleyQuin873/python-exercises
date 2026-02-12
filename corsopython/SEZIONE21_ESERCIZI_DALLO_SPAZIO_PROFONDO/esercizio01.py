import math

class Astronave:
    x = 0  # posizione attuale dell'atronave
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def muovi_a(self,dest_x, dest_y):
        self.x = dest_x
        self.y = dest_y
        print(f"L'astronave si è mossa alle coordinate ({self.x}, {self.y}).")
    
    def distanza_da(self,dest_x, dest_y) -> float:
        #distanza euclidea
        d = math.sqrt((dest_x - self.x)**2 + (dest_y - self.y)**2)
        return d

Nabuccodonosor = Astronave(0,0)

Nabuccodonosor.muovi_a(5,5)

d = Nabuccodonosor.distanza_da(0,0)

print("Distanza da(5,5): ", d)
print(f"L'astronave è a {d} unità dall'origine.")


