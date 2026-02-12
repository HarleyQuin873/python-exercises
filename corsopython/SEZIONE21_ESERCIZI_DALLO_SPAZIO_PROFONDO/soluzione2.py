class Pianeta:
    def __init__(self, nome, risorse):
        self.nome = nome
        self.risorse = risorse


class Astronave:
    def __init__(self, capacita_carico):
        self.capacita_carico = capacita_carico
        self.carico_attuale = 0
        self.risorse_raccolte = {}

    @staticmethod
    def messaggio_esplorazione(nome_pianeta):
        return f"Esplorando il pianeta {nome_pianeta}..."

    @classmethod
    def astronave_standard(cls):
        return cls(capacita_carico=150)

    def capacita_rimanente(self):
        return self.capacita_carico - self.carico_attuale

    def _puo_caricare(self, massa):
        return self.carico_attuale + massa <= self.capacita_carico

    def esplora(self, pianeta):
        print(Astronave.messaggio_esplorazione(pianeta.nome))

        for risorsa, massa in pianeta.risorse.items():
            if self._puo_caricare(massa):
                self.carico_attuale += massa
                self.risorse_raccolte[risorsa] = self.risorse_raccolte.get(risorsa, 0) + massa
                print(f"Raccolta la risorsa {risorsa} con massa {massa}!")
            else:
                print(f"Impossibile raccogliere ulteriormente {risorsa} a causa della capacità di carico!")


# Creiamo alcuni pianeti con diverse risorse e masse
terra = Pianeta("Terra", {'ferro': 50, 'oro': 25})
marte = Pianeta("Marte", {'ferro': 30, 'argento': 40})
giove = Pianeta("Giove", {'platino': 90, 'oro': 120})

# Creiamo un'astronave usando il metodo di classe
voyager = Astronave.astronave_standard()

# L'astronave esplora i pianeti e raccoglie risorse
voyager.esplora(terra)
voyager.esplora(marte)
voyager.esplora(giove)

print("\nRisorse raccolte dall'astronave:")
for risorsa, massa in voyager.risorse_raccolte.items():
    print(f"{risorsa}: {massa}")
