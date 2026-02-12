from pathlib import Path 

# path = Path(r"C:\Users\PC\Desktop\Corsi di sviluppo\corso_py\corsopython\GESTIONE_DEI_FILE", "codice", "isolamisteriosa.txt")

# f = open(path)

# home= Path.home()

# path = Path(r"C:\Users\PC\Desktop\Corsi di sviluppo\corso_py\corsopython\GESTIONE_DEI_FILE", "codice", "isolamisteriosa.txt")

# f= open(path)

# file_object = open(isolamisteriosa.txt, read )

# file_object = open('isolamisteriosa.txt', 'r')

# try:
#    # Apri il file in modalità lettura
#    file_object = open('isolamisteriosa.txt', 'r')
    
#   #  Leggi il contenuto del file
#    content = file_object.read()

#    content = file_object.read()
#    line = file_object.readline()
#    print(line)
#    # Stampa il contenuto del file
#    print(content)

#    print(content)
#    print(file_object.encoding)


#    with open("isolamisteriosa.txt", "rt") as f:
#        counter=0
#        for line in f:
#            counter += 1
#            print(f"{counter}:{line}")

# with open("isolamisteriosa.txt", "rt") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# finally:
#     # Assicurati che il file venga chiuso
#     file_object.close()
#     f.close()

# # Apri il file "isolamisteriosa.txt" in modalità lettura (testo)
# with open("isolamisteriosa.txt", "rt") as f:
#     # 'with' garantisce che il file venga chiuso automaticamente alla fine del blocco

#     # Leggi tutte le righe del file e salvale in una lista chiamata 'lines'
#     lines = f.readlines()

#     # Ciclo che scorre ogni riga nella lista 'lines'
#     for line in lines:
#         # Stampa la riga corrente
#         print(line)





with open("isolamisteriosa.txt", "rt") as f:
    lines = f.readlines()
    for line in lines:
        print(line)







