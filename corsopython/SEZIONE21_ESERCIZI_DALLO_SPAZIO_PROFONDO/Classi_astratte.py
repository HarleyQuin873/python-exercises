#esercizio06

from abc import ABC, abstractmethod
from typing import List, Protocol

#Definizione della classe astratta
class Observer(ABC):
    @abstractmethod
    def aggiorna(self, status):
        pass

class Subject(ABC):

    _observers = []   #lista di observer

    @abstractmethod
    def aggiungi_observer(self, observer):
        pass

    def rimuovi_observer(self,observer):
        pass

    @abstractmethod
    def notifica_observers(self,status):
        pass

class SistemaDiAllarme(Subject):

    def __init__(self):
        super().__init__()
        self._is_active = None
        self._observers = [] #lista di observer

    def attiva_allarme(self):
        #attiva il sistema di Allarme
        print("Allarme attivato!")
        self._is_active = True
        self.notifica_observers(self._is_active)

    def disattiva_allarme(self):
        print("Allarme disattivato!")
        #disattiva il sistema di allarme
        self._is_active=False
        self.notifica_observers(self._is_active)

    def get_status(self):
        return self._is_active

    def aggiungi_observer(self,observer):
        self._observers.append(observer)
        print(f"Observer: {observer} aggiunto!")

    def rimuovi_observer(self, observer):
        self._observers.remove(observer)
        print(f"Observer: {observer} rimosso!")

    def notifica_observers(self,status):
        if(status):
            self._is_active=True
            for o in self._observers:
                o.aggiorna(self._is_active)
        else:
            self._is_active= False
            for o in self._observers:
                o.aggiorna(self._is_active)

class PonteComando(Observer):
    def aggiorna(self,status):
        if(status):
            print("Ponte di Comando: BLOCCA TUTTE LE ENTRATE E LE USCITE!")
        else:
            print("POnte di Comando: RIAPERTURA DELLE ENTRATE E DELLE USCITE")

    def __str__(self) -> str:
        return "Ponte di Comando"

class SalaMotori(Observer):
    def aggiorna(self, status):
        if(status):
            print("Sala Motori: Preparazione per manovra evasiva.")
        else:
            print("Sala Motori: Preparazione della normale operatività")

    def __str__(self)-> str:
        return "Sala Motori"

class CabineEquipaggio(Observer):
    def aggiorna(self, status):
        if(status):
            print("Cabine dell'equipaggio: TUTTI ALL'INTERNO, METTERSI IN SICUREZZA!")
        else:
            print("Cabine dell'equipaggio: TUTTO è TORNATO ALLA NORMALITA'")
        
    def __str__(self)->str:
        return "Cabine dell'Equipaggio"

sistema_allarme = SistemaDiAllarme()

ponte_comando = PonteComando()

sala_motori = SalaMotori()

cabine_equipaggio = CabineEquipaggio()

sistema_allarme.aggiungi_observer(ponte_comando)
sistema_allarme.aggiungi_observer(sala_motori)
sistema_allarme.aggiungi_observer(cabine_equipaggio)

sistema_allarme.attiva_allarme()
sistema_allarme.disattiva_allarme()

sistema_allarme.rimuovi_observer(sala_motori)
sistema_allarme.attiva_allarme()
sistema_allarme.disattiva_allarme()



