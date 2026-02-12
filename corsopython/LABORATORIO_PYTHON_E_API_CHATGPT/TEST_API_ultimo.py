# Importazione della libreria openai
from openai import OpenAI

# Creazione di un client OpenAI, passando la tua API key per l'autenticazione.
# Nota: la chiave API è un valore sensibile, quindi sarebbe più sicuro memorizzarla come variabile d'ambiente
# o in un file di configurazione piuttosto che nel codice.
client = OpenAI(api_key="")

# Lista per memorizzare la cronologia della conversazione (sia quella dell'utente che della risposta del modello).
chat_history = []

# Ciclo infinito che continua a ricevere input dall'utente fino a quando non si digita "stop".
while True:
    # Chiede all'utente di inserire un input (domanda o richiesta per il modello).
    user_input = input("\nUser: ")
    
    # Aggiunge il messaggio dell'utente alla cronologia della conversazione
    chat_history.append({"role": "user", "content": user_input})
    
    # Se l'utente digita "stop", esce dal ciclo e termina il programma
    if user_input.lower() == "stop":
        break

    # Effettua una richiesta al modello OpenAI per generare una risposta sulla base della cronologia della conversazione.
    # La richiesta viene fatta in modalità "stream", che consente di ricevere la risposta del modello in tempo reale (a pezzi).
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # Il modello specificato per la generazione della risposta.
        messages=chat_history,       # Passa la cronologia dei messaggi (sia dell'utente che delle risposte precedenti).
        stream=True                  # Abilita lo streaming per ottenere risposte parziali man mano che vengono generate.
    )

    # Ciclo attraverso ogni "pezzo" della risposta generata in tempo reale
    for chunk in stream:
        # Controlla se la parte della risposta contiene effettivamente del contenuto da visualizzare.
        # Ogni "chunk" contiene una parte della risposta generata, e `delta.content` è la porzione di testo
        # che il modello ha appena prodotto.
        if chunk.choices[0].delta.content is not None:
            # Stampa il contenuto della risposta generata senza andare a capo, per continuare la risposta su una singola riga.
            print(chunk.choices[0].delta.content, end="")

