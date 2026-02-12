from pathlib import Path

with open("isolamisteriosa.txt", "rt") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# Apre due file contemporaneamente usando 'with' per garantire la chiusura automatica dei file
# - 'fin' è il file di input (in modalità lettura "rt")
# - 'fout' è il file di output (in modalità append "a")
# with (
#     open("isolamisteriosa.txt", "rt") as fin,   # Apre il file di input in modalità lettura
#     open("outputfile.txt", "a") as fout        # Apre il file di output in modalità aggiunta (append)
#     ):

#     # Leggi tutte le righe dal file di input e salvale nella lista 'lines'
#     lines = fin.readlines()

#     # Inizializza il contatore delle righe
#     c = 1

#     # Ciclo che scorre ogni riga nella lista 'lines'
#     for l in lines:
#         # Verifica se il numero della riga è pari (c % 2 == 0)
#         # if(c % 2 == 0):
#             # Crea una stringa che unisce il numero della riga e il contenuto della riga
#         str = f"{c}:{l}"

#             # Scrive la stringa nel file di output
#         fout.write(str)

#         # Incrementa il contatore per passare alla riga successiva
#         c += 1







# with open("isolamisteriosa.txt", "rt") as fin, \
#      open("outputfile.txt", "a") as fout:
    
#     lines = fin.readlines()
#     c = 1

#     for l in lines:
#         if c%2==0:
#             str = f"{c}:{l}"
#             fout.write(str) 
#         c += 1






with open("isolamisteriosa.txt", "rt") as fin, \
     open("outputfile.txt", "a") as fout:
    lines=fin.readlines()

    c=1
    for l in lines:
        if c%2==0:
            str=f"{c}:{l}"
            fout.write(str)
        c += 1