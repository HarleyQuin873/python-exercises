import openai
import time

# Configura l'API key di OpenAI
openai.api_key = ''


def create_completion(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sei un assistente utile."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        print(f"Errore durante la chiamata API: {e}")
        return None

# Esempio di utilizzo della funzione
prompt = "Ciao, come stai?"
completion = create_completion(prompt)
if completion:
    print("Risposta:", completion)
else:
    print("Non è stato possibile ottenere una risposta.")
