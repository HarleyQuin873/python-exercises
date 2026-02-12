from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def aggiorna(self, status: bool):
        pass

# Subject
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def aggiungi_observer(self, observer: Observer):
        self._observers.append(observer)

    def rimuovi_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notifica_observers(self, status: bool):
        for observer in self._observers:
            observer.aggiorna(status)

# Concrete Subject
class SistemaDiAllarme(Subject):
    def __init__(self):
        super().__init__()
        self._is_active = False

    def attiva_allarme(self):
        self._is_active = True
        self.notifica_observers(self._is_active)

    def disattiva_allarme(self):
        self._is_active = False
        self.notifica_observers(self._is_active)

class PonteComando(Observer):
    def aggiorna(self, status: bool):
        if status == True:
            print("Ponte di Comando: Bloccando tutte le entrate e uscite.")
        else:
            print("Ponte di Comando: Riapertura delle entrate e uscite.")

class SalaMotori(Observer):
    def aggiorna(self, status: bool):
        if status == True:
            print("Sala Motori: Preparazione per manovra evasiva.")
        else:
            print("Sala Motori: Ripresa della normale operatività.")

class CabineEquipaggio(Observer):
    def aggiorna(self, status: bool):
        if status == True:
            print("Cabine dell'Equipaggio: Tutti all'interno, mettersi in sicurezza!")
        else:
            print("Cabine dell'Equipaggio: Tutto è tornato alla normalità.")

if __name__ == "__main__":
    # Creazione del sistema di allarme
    allarme = SistemaDiAllarme()

    # Creazione delle varie sezioni (osservatori)
    ponte_comando = PonteComando()
    motori = SalaMotori()
    cabine = CabineEquipaggio()

    # Aggiunta degli osservatori al sistema di allarme
    allarme.aggiungi_observer(ponte_comando)
    allarme.aggiungi_observer(motori)
    allarme.aggiungi_observer(cabine)

    # Simulazione di un allarme
    print("\nSimulazione primo allarme:")
    allarme.attiva_allarme()

    # Simulazione della fine dell'allarme
    print("\nFine  primo allarme:")
    allarme.disattiva_allarme()

    allarme.rimuovi_observer(motori)

    # Simulazione di un allarme
    print("\nSimulazione secondo allarme:")
    allarme.attiva_allarme()

    # Simulazione della fine dell'allarme
    print("\nFine secondo allarme:")
    allarme.disattiva_allarme()
