from abc import ABC, abstractmethod

class ComponentAstronave(ABC):

    def __init__(self,nome):
        self.nome = nome
    
    @abstractmethod
    def operazione(self,livello):
        pass

   # @abstractmethod
    def aggiungi(Component):
        pass
    
   # @abstractmethod
    def rimuovi(Component):
        pass

 #   @abstractmethod
    def ottieniFiglio(int):
        pass

    
class Sistema(ComponentAstronave):

    def __init__(self,nome):
        super().__init__(nome)

    def operazione(self,livello):
        print('  ' * livello + f"{self.nome}")

class ModuloComplesso(ComponentAstronave):

    def __init__(self,nome):
        super().__init__(nome)
        self.nome = nome
        self._children = []

    def operazione(self,livello):
        print('  ' * livello + f"{self.nome}:")
        for i in self._children:
            i.operazione(livello + 1)

    def aggiungi(self,Component):
        self._children.append(Component)
    
   
    def rimuovi(self,Component):
        self._children.remove(Component)

    
    def ottieniFiglio(self,i:int):
        if i < 0 or i >= len(self._children):
            return None
        return self._children[i]

        
#creazione di modulo e foglie
Andromeda = ModuloComplesso("Andromeda")
ponte_di_comando = ModuloComplesso("Ponte di comando")
modulo_navigazione = ModuloComplesso("Modulo di navigazione")
sala_motori = ModuloComplesso("Sala Motori")
motore1 = Sistema("Motore 1")
motore2 = Sistema("Motore 2")
motore3 = Sistema("Motore 3")
modulo_difesa = ModuloComplesso("Modulo di difesa")
scudo = Sistema("Scudo 1")
scudo2 = Sistema("Scudo 2")
scudo3 = Sistema("Scudo 3")

sistema_allarme_observer = ModuloComplesso("Sistema di allarme Observer")
sistema_di_comunicazione = Sistema("Sistema di comunicazione")
computer_centrale = Sistema("Computer Centrale")

deposito = Sistema("Deposito")
risorse_raccolte = Sistema("Risorse raccolte")
magazzino = ModuloComplesso("Magazzino")
archivio = ModuloComplesso("Archivio")
report1 = Sistema("report1")
report2 = Sistema("report2")
cucine = Sistema("Cucine")
cabine_equipaggio = ModuloComplesso("Cabine dell'equipaggio")
cabina1 = Sistema("Cabina 1")
cabina2 = Sistema("Cabina 2")
cabina3 = Sistema("Cabina 3")

moduli_scientifici = ModuloComplesso("Moduli scientifici")

Nebula = ModuloComplesso("Nebula")
Galileo = ModuloComplesso("Galileo")
Celestia = ModuloComplesso("Celestia")

mappatura_stellare = ModuloComplesso("Sistema di mappatura stellare")
sezioni_spazio_identificate = ModuloComplesso("Sezioni di spazio identificate")
stelle = Sistema("Stelle")
pianeti = ModuloComplesso("Pianeti")
nebulose = Sistema("Nebulose")
corpi_celesti = Sistema("Corpi celesti")
pianeta1 = Sistema("Venere")
pianeta2 = Sistema("Sole")
pianeta3 = Sistema("Luna")
pianeta4 = Sistema("Marte")
pianeta5 = Sistema("Giove")
pianeta6 = Sistema("Saturno")
pianeta7 = Sistema("Terra")
pianeta8 = Sistema("Saturno")
pianeta9 = Sistema("Nettuno")
pianeta10 = Sistema("Urano")
pianeta11 = Sistema("Mercurio")
pianeta12 = Sistema("Plutone")
pianeta13 = Sistema("Eris")
pianeta14 = Sistema("Haumea")
pianeta15 = Sistema("Makemake")
pianeta16 = Sistema("Ceres")
Sistema_analisi_spettrale = ModuloComplesso("Sistema analisi spettrale")
spettri_trovati = Sistema("Spettri trovati")

sistemi_rilevazione_particelle = ModuloComplesso("Sistemi di rilevazione particelle")
s1 = Sistema("sistema 1 di rilevazione particelle")
s2 = Sistema("sistema 2 di rilevazione particelle")
s3 = Sistema("sistema 3 di rilevazione particelle")
strumenti_analisi_chimica = ModuloComplesso("Strumenti di analisi chimica")
sac = Sistema("Sistema di analisi chimica 1")
sac2 = Sistema("Sistema di analisi chimica 2")
sac3 = Sistema("Sistema di analisi chimica 3")

studio_radiazione_cosmica = ModuloComplesso("Studio radiazione cosmica")
esperimenti_radiazioni = ModuloComplesso("Esperimenti sulle radiazioni")
esperimento1 = Sistema("Esperimento 1 sulle radiazioni cosmiche")
esperimento2 = Sistema("Esperimento 2 sulle radiazioni cosmiche")
esperimento3 = Sistema("Esperimento 3 sulle radiazioni cosmiche")
studio_particelle_subatomiche = ModuloComplesso("Studio delle particelle subatomiche")
esperimenti_particelle = ModuloComplesso("Esperimenti sulle particelle subatomiche")
e1 = Sistema("Esperimento 1 sulle particelle subatomiche")
e2 = Sistema("Esperimento 2 sulle particelle subatomiche")
e3 = Sistema("Esperimento 3 sulle particelle subatomiche")

studio_ambientale=ModuloComplesso("Studio ambientale")
organismi_viventi= Sistema("Organismi viventi")
ambiente_controllato = Sistema("Ambiente controllato")
studio_impatto_condizioni=ModuloComplesso("Studio dell'impatto delle condizioni spaziali sulla vita biologica")
esperimenti =ModuloComplesso("Esperimenti ")
e11 = Sistema("Esperiemnto 11")
e22 = Sistema("Esperimento 22")
e33 = Sistema("Esperimento 33")


#costruzione della struttura ad albero

Andromeda.aggiungi(ponte_di_comando)
Andromeda.aggiungi(moduli_scientifici)

ponte_di_comando.aggiungi(modulo_navigazione)
ponte_di_comando.aggiungi(sistema_allarme_observer)

modulo_navigazione.aggiungi(sala_motori)
modulo_navigazione.aggiungi(modulo_difesa)

sala_motori.aggiungi(motore1)
sala_motori.aggiungi(motore2)
sala_motori.aggiungi(motore3)

modulo_difesa.aggiungi(scudo)
modulo_difesa.aggiungi(scudo2)
modulo_difesa.aggiungi(scudo3)

sistema_allarme_observer.aggiungi(sistema_di_comunicazione)
sistema_allarme_observer.aggiungi(computer_centrale)
sistema_allarme_observer.aggiungi(magazzino)
sistema_allarme_observer.aggiungi(cucine)
sistema_allarme_observer.aggiungi(cabine_equipaggio)

magazzino.aggiungi(deposito)
magazzino.aggiungi(risorse_raccolte)
magazzino.aggiungi(archivio)

archivio.aggiungi(report1)
archivio.aggiungi(report2)

cabine_equipaggio.aggiungi(cabina1)
cabine_equipaggio.aggiungi(cabina2)
cabine_equipaggio.aggiungi(cabina3)

moduli_scientifici.aggiungi(Nebula)
moduli_scientifici.aggiungi(Galileo)
moduli_scientifici.aggiungi(Celestia)

Nebula.aggiungi(mappatura_stellare)
Nebula.aggiungi(Sistema_analisi_spettrale)

mappatura_stellare.aggiungi(sezioni_spazio_identificate)

sezioni_spazio_identificate.aggiungi(stelle)
sezioni_spazio_identificate.aggiungi(pianeti)
sezioni_spazio_identificate.aggiungi(nebulose)
sezioni_spazio_identificate.aggiungi(corpi_celesti)

pianeti.aggiungi(pianeta1)
pianeti.aggiungi(pianeta2)
pianeti.aggiungi(pianeta3)
pianeti.aggiungi(pianeta4)
pianeti.aggiungi(pianeta5)
pianeti.aggiungi(pianeta6)
pianeti.aggiungi(pianeta7)
pianeti.aggiungi(pianeta8)
pianeti.aggiungi(pianeta9)
pianeti.aggiungi(pianeta10)
pianeti.aggiungi(pianeta11)
pianeti.aggiungi(pianeta12)
pianeti.aggiungi(pianeta13)
pianeti.aggiungi(pianeta14)
pianeti.aggiungi(pianeta15)
pianeti.aggiungi(pianeta16)

Sistema_analisi_spettrale.aggiungi(spettri_trovati)

Galileo.aggiungi(sistemi_rilevazione_particelle)
Galileo.aggiungi(strumenti_analisi_chimica)
Galileo.aggiungi(studio_radiazione_cosmica)
Galileo.aggiungi(studio_particelle_subatomiche)

sistemi_rilevazione_particelle.aggiungi(s1)
sistemi_rilevazione_particelle.aggiungi(s2)
sistemi_rilevazione_particelle.aggiungi(s3)

strumenti_analisi_chimica.aggiungi(sac)
strumenti_analisi_chimica.aggiungi(sac2)
strumenti_analisi_chimica.aggiungi(sac3)

studio_radiazione_cosmica.aggiungi(esperimenti_radiazioni)

esperimenti_radiazioni.aggiungi(esperimento1)
esperimenti_radiazioni.aggiungi(esperimento2)
esperimenti_radiazioni.aggiungi(esperimento3)

studio_particelle_subatomiche.aggiungi(esperimenti_particelle)
esperimenti_particelle.aggiungi(e1)
esperimenti_particelle.aggiungi(e2)
esperimenti_particelle.aggiungi(e3)

Celestia.aggiungi(studio_ambientale)

studio_ambientale.aggiungi(organismi_viventi)
studio_ambientale.aggiungi(ambiente_controllato)
studio_ambientale.aggiungi(studio_impatto_condizioni)

studio_impatto_condizioni.aggiungi(esperimenti)

esperimenti.aggiungi(e11)
esperimenti.aggiungi(e22)
esperimenti.aggiungi(e33)

#visualizzazione della struttura
Andromeda.operazione(0)
