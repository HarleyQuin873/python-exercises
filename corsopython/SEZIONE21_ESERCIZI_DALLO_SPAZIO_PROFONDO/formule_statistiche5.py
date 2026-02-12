import numpy as np
import scipy.stats as stats

# Dati di esempio
dati = np.array([10, 20, 30, 40, 50])

# 1. Statistiche Descrittive

# Media
media = np.mean(dati)

# Mediana
mediana = np.median(dati)

# Moda
moda_result = stats.mode(dati)
moda = moda_result.mode if isinstance(moda_result.mode, np.ndarray) and len(moda_result.mode) > 0 else None

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


# 2. Statistiche Inferenziali

# Z-Score (per un valore specifico, ad esempio 30)
z_score = (30 - media) / deviazione_standard
print(f"Z-Score per 30: {z_score}")

# Intervallo di confidenza (ad esempio per il 95%)
confidence_level = 0.95
z_value = stats.norm.ppf((1 + confidence_level) / 2)  # valore critico per un intervallo di confidenza di 95%
errore_standard = deviazione_standard / np.sqrt(len(dati))
intervallo_confidenza = (media - z_value * errore_standard, media + z_value * errore_standard)

