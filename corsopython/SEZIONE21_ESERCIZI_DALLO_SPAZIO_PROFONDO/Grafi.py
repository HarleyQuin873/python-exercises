#esercizio07

class CorpoCeleste:
    def __init__(self,nome):
        self.nome=nome
        self.distanza= 0
        self.adiacenti=[]


    def aggiungi_collegamento(self, nome, distanza):
        self.adiacenti.append((nome, distanza))  # Aggiungi una tupla
        print(f"Collegamento aggiunto fra il nodo {self.nome} e il nodo {nome}")

    def rimuovi_collegamento(self, nome, distanza):
        self.adiacenti.remove((nome,distanza))
        print(f"Collegamento rimosso fra il nodo {self.nome} e il nodo {nome}")

    def __str__(self):
        risultato = f"Corpi celesti adiacenti al nodo {self.nome}: "
        risultato += ", ".join(f"{nome}:{distanza}" for nome, distanza in self.adiacenti) 
        return risultato

    def __repr__(self):
        return f"{self.nome}: {self.adiacenti}"

class MappaStellare:

    def __init__(self):
        self.corpi_celesti=[]

    def aggiungi_corpo_celeste(self, corpo_celeste):
        c = CorpoCeleste(corpo_celeste)
        self.corpi_celesti.append(c)
        print(f"Corpo celeste {c.nome} aggiunto alla mappa stellare.")

    def rimuovi_corpo_celeste(self, corpo_celeste):
        # Trova il corpo celeste nella lista usando il nome
        corpo_celeste_da_rimuovere=None
        for corpo in self.corpi_celesti:
            if corpo.nome == corpo_celeste.nome:
                corpo_celeste_da_rimuovere = corpo
                break

        if corpo_celeste_da_rimuovere:
            # Rimuovi collegamenti adiacenti
            for adiacente in corpo_celeste_da_rimuovere.adiacenti:
                corpo_celeste_da_rimuovere.rimuovi_collegamento(adiacente[0], adiacente[1])
            #self.corpi_celesti.remove(corpo_celeste)

            # Rimuovi il corpo celeste dalla lista
            self.corpi_celesti.remove(corpo_celeste_da_rimuovere)
            print(f"Corpo celeste {corpo_celeste.nome} rimosso dalla mappa stellare.")
        else:
            print(f"Corpo celeste {corpo_celeste.nome} non trovato nella mappa stellare.")


    def aggiungi_percorso(self, partenza, arrivo, distanza):
        if partenza in self.corpi_celesti and arrivo in self.corpi_celesti:
            self.corpi_celesti[partenza].aggiungi_collegamento(partenza,distanza)
            self.corpi_celesti[arrivo].aggiungi_collegamento(arrivo.distanza)
        else:
            print(f"I corpi celesti {partenza} e/o {arrivo} non sono nella mappa stellare.")

    def __str__(self):
        return "\n".join(str(corpo) for corpo in self.corpi_celesti)


pianeta1 = CorpoCeleste("Venere")
pianeta2 = CorpoCeleste("Sole")
pianeta3 = CorpoCeleste("Luna")
pianeta4 = CorpoCeleste("Marte")
pianeta5 = CorpoCeleste("Giove")
pianeta6 = CorpoCeleste("Saturno")
pianeta7 = CorpoCeleste("Terra")
pianeta8 = CorpoCeleste("Nettuno")
pianeta9 = CorpoCeleste("Urano")
pianeta10 = CorpoCeleste("Mercurio")
pianeta11 = CorpoCeleste("Plutone")
pianeta12 = CorpoCeleste("Eris")
pianeta13 = CorpoCeleste("Haumea")
pianeta14 = CorpoCeleste("Makemake")
pianeta15 = CorpoCeleste("Ceres")

mappa_stellare=MappaStellare()

mappa_stellare.aggiungi_corpo_celeste(pianeta1)
mappa_stellare.aggiungi_corpo_celeste(pianeta2)
mappa_stellare.aggiungi_corpo_celeste(pianeta3)
mappa_stellare.aggiungi_corpo_celeste(pianeta4)
mappa_stellare.aggiungi_corpo_celeste(pianeta5)
mappa_stellare.aggiungi_corpo_celeste(pianeta6)
mappa_stellare.aggiungi_corpo_celeste(pianeta7)
mappa_stellare.aggiungi_corpo_celeste(pianeta8)
mappa_stellare.aggiungi_corpo_celeste(pianeta9)
mappa_stellare.aggiungi_corpo_celeste(pianeta10)
mappa_stellare.aggiungi_corpo_celeste(pianeta11)
mappa_stellare.aggiungi_corpo_celeste(pianeta12)
mappa_stellare.aggiungi_corpo_celeste(pianeta13)
mappa_stellare.aggiungi_corpo_celeste(pianeta14)
mappa_stellare.aggiungi_corpo_celeste(pianeta15)

pianeta1.aggiungi_collegamento("Sole", 10)
pianeta1.aggiungi_collegamento("Luna", 500)

pianeta2.aggiungi_collegamento("Venere", 10)
pianeta2.aggiungi_collegamento("Giove", 100)

pianeta3.aggiungi_collegamento("Venere", 500)

pianeta4.aggiungi_collegamento("Makemake", 50)

pianeta5.aggiungi_collegamento("Sole", 100)
pianeta5.aggiungi_collegamento("Saturno", 200)

pianeta6.aggiungi_collegamento("Giove", 200)
pianeta6.aggiungi_collegamento("Haumea", 400)

pianeta7.aggiungi_collegamento("Nettuno", 300)

pianeta8.aggiungi_collegamento("Terra", 300)
pianeta8.aggiungi_collegamento("Ceres", 900)

pianeta9.aggiungi_collegamento("Ceres", 33)

pianeta10.aggiungi_collegamento("Eris", 22)

pianeta11.aggiungi_collegamento("Eris", 1000)

pianeta12.aggiungi_collegamento("Mercurio", 222)
pianeta12.aggiungi_collegamento("Plutone", 1000)
pianeta12.aggiungi_collegamento("Ceres", 800)

pianeta13.aggiungi_collegamento("Saturno", 400)
pianeta13.aggiungi_collegamento("Ceres", 600)

pianeta14.aggiungi_collegamento("Marte", 50)
pianeta14.aggiungi_collegamento("Ceres", 700)

pianeta15.aggiungi_collegamento("Haumea", 600)
pianeta15.aggiungi_collegamento("Makemake", 700)
pianeta15.aggiungi_collegamento("Eris", 800)
pianeta15.aggiungi_collegamento("Urano", 33)
pianeta15.aggiungi_collegamento("Nettuno", 900)

print(f"Mappa stellare: {mappa_stellare}" )

print(f"Rimuovi corpo celeste: {pianeta15}.")
mappa_stellare.rimuovi_corpo_celeste(pianeta15 )

print("Mappa stellare: ", mappa_stellare)



