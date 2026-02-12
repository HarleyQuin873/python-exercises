from enum import Enum

class PuntoCardinale(Enum):
    NORD = 'N'
    SUD = 'S'
    EST = 'E'
    OVEST = 'O'

for direzione in PuntoCardinale:
    print(f"Nome: {direzione.name}, Valore: {direzione.value}")

direzione_scelta= PuntoCardinale.NORD
if direzione_scelta == PuntoCardinale.NORD:
    print("Stai andando verso nord!") 