for i in range(2): # Alla prima iterazione 'i' varrà 0 e alla seconda 1
    if i % 2 == 0:
        print("Sono all'interno del blocco if, per cui...")
        print(i, "e' un numero pari.\n")
        continue # riprendi dalla prima istruzione del ciclo 'for'
    print("Il blocco if e' stato saltato, per cui...")
    print(i, "e' un numero dispari\n")