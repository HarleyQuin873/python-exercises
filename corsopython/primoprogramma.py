print("Corso Python")

def paridispari():
    inp = input("Inserisci un numero: ")
    numero = int(inp)
    modulo = numero % 2
    if modulo == 0:
        print("Numero pari")
    else:
        print("Numero dispari")