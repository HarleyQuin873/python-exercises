class Comunicazione:
    def __init__(self, mittente, messaggio):
        self.mittente=mittente
        self.messaggio=messaggio
    
    def __str__(self):
        return f"Da {self.mittente}: {self.messaggio}"

class StackComunicazioni:
    def __init__(self, capacita=10):
        self.comunicazioni = []
        self.capacita=capacita

    def push(self,comunicazione):
        if self.size() < self.capacita:
            self.comunicazioni.append(comunicazione)
            print(f"\nAggiunto messaggio: {comunicazione}")
        else:
            print(f"\nErrore: capacità massima raggiunta")


    def pop(self):
        if not self.is_empty():
            return self.comunicazioni.pop()
        else:
            print("Errore! Lo stack è vuoto!")
            return None

    def peek(self):
        if not self.is_empty():
            return self.comunicazioni[-1]
        else:
            return None
        
    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.comunicazioni)

stack_comunicazioni = StackComunicazioni(3)

com1 = Comunicazione("Pianeta A", "Saluti all'equipaggio di Andromeda!")
com2 = Comunicazione("Pianeta B", "Richiesta di assistenza urgente!")
com3 = Comunicazione("Pianeta C", "Invio risorse e beni.")
com4 = Comunicazione("Pianeta D", "Festa galattica prevista per domani")

stack_comunicazioni.push(com1)
stack_comunicazioni.push(com2)
stack_comunicazioni.push(com3)
stack_comunicazioni.push(com4)

ultima_comunicazione = stack_comunicazioni.peek()

if ultima_comunicazione:
    print(f"Ultima comunicazione ricevuta: {ultima_comunicazione}")

comunicazione_rimossa = stack_comunicazioni.pop()
if ultima_comunicazione:
    print(f"Rimossa ultima comunicazione ricevuta: {ultima_comunicazione}")

ultima_comunicazione = stack_comunicazioni.peek()

if ultima_comunicazione:
    print(f"Ultima comunicazione ricevuta: {ultima_comunicazione}")

stack_comunicazioni.pop()
stack_comunicazioni.pop()

#stack_comunicazioni.pop()
