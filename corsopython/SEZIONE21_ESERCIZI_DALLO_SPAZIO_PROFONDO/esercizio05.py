class Comunicazione:

    def __init__(self,mittente,messaggio):
        self.mittente = mittente
        self.messaggio = messaggio

    def __str__(self):
        return f"Da {self.mittente}: {self.messaggio}"
    
class StackComunicazioni:

    def __init__(self,capacita):
        self.capacita = capacita
        self.items = []

    def is_empty(self):
        #Verifica se lo stack è vuoto."""
        return len(self.items) == 0

    def size(self):
         return len(self.items)

    def push(self,messaggio):
        #aggiunge un elemento al top dello StackComunicazioni
        # self.items.append(messaggio)

        if self.size() < self.capacita:
            self.items.append(messaggio)
            print(f"\nAggiunto messaggio: {messaggio}")
        else:
            print("\nErrore: capacità massima raggiunta!")  

    def pop(self)->str:
        #restituisce e rimuove il messaggio in cima allo StackComunicazioni
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        else: 
            return self.items.pop()
    
    def peek(self)->str:
        #restituisce il messaggio presente al top dello stack
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def __str__(self):
        # """Restituisce una rappresentazione a stringa dello stack."""
        # return print("Stack: " + str(self.items))
        return f"Da {self.mittente}: {self.messaggio}"    
        
stack_comunicazioni = StackComunicazioni(3)

com1 = Comunicazione("Pianeta A", "Saluti all'equipaggio di Andromeda!")
com2 = Comunicazione("Pianeta B", "Richiesta di assistenza urgente.")
com3 = Comunicazione("Pianeta C", "Invio risorse e beni.")
com4 = Comunicazione("Pianeta D", "Festa galattica prevista per domani!")

stack_comunicazioni.push(com1)
stack_comunicazioni.push(com2)
stack_comunicazioni.push(com3)

stack_comunicazioni.push(com4) 

ultima_comunicazione = stack_comunicazioni.peek()
if ultima_comunicazione:
    print(f"\nUltima Comunicazione ricevuta: {ultima_comunicazione}")

comunicazione_rimossa = stack_comunicazioni.pop()
if ultima_comunicazione:
    print(f"\nRimossa Ultima Comunicazione ricevuta: {ultima_comunicazione}")

ultima_comunicazione = stack_comunicazioni.peek()
if ultima_comunicazione:
    print(f"\nUltima Comunicazione ricevuta: {ultima_comunicazione}")

stack_comunicazioni.pop()
stack_comunicazioni.pop()

stack_comunicazioni.pop()  # Questo dovrebbe generare un errore di underflow
