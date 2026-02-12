import numpy as np
import scipy.stats as stats

# Dati di esempio
dati = np.array([10, 20, 30, 40, 50])

# Media
media = np.mean(dati)

# Mediana
mediana = np.median(dati)

# Moda
moda_result = stats.mode(dati)
moda = moda_result.mode[0] if len(moda_result.mode) > 0 else None  # Verifica che ci sia almeno una moda

# Varianza
varianza = np.var(dati)

# Deviazione standard
deviazione_standard = np.std(dati)

# Range
range_dati = np.max(dati) - np.min(dati)

# Risultati delle statistiche descrittive
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Varianza: {varianza}")
print(f"Deviazione Standard: {deviazione_standard}")
print(f"Range: {range_dati}")
