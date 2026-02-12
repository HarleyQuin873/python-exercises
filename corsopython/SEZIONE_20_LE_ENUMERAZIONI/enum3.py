from enum import Enum

class StatoSemaforo(Enum):
    ROSSO = 1
    GIALLO = 2
    VERDE = 3

print(StatoSemaforo.ROSSO == StatoSemaforo.ROSSO)
print(StatoSemaforo.ROSSO == StatoSemaforo.VERDE)
print(StatoSemaforo.ROSSO is StatoSemaforo.ROSSO)
print(StatoSemaforo.ROSSO is StatoSemaforo.VERDE)
print(StatoSemaforo.ROSSO == 1)

