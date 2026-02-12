import openai
import time

# Configura l'API key di OpenAI
openai.api_key = ''

def create_completion(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError:
        print("Superato il limite di richieste API. Ritenta tra un po'.")
        return None

# Esempio di utilizzo della funzione
prompt = "Ciao, come stai?"
completion = create_completion(prompt)
if completion:
    print("Risposta:", completion)
else:
    print("Non è stato possibile ottenere una risposta.")
