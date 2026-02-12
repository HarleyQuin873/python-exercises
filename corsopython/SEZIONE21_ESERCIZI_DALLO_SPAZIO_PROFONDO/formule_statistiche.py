import numpy as np
import scipy.stats as stats

# 1. Statistiche Descrittive

# Dati di esempio
dati = np.array([10, 20, 30, 40, 50])

# Media
media = np.mean(dati)

# Mediana
mediana = np.median(dati)

# Moda
moda = stats.mode(dati).mode[0]
# stats.mode(dati)[0][0]  # scipy.stats.mode restituisce un oggetto, quindi prendo il primo valore

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
print(f"Intervallo di confidenza 95%: {intervallo_confidenza}")


# 3. Correlazione e Regressione

# Dati di esempio (due variabili)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Coefficiente di correlazione di Pearson
correlazione = np.corrcoef(x, y)[0, 1]
print(f"Coefficiente di correlazione di Pearson: {correlazione}")

# Regressione lineare (usiamo la funzione polyfit di numpy)
slope, intercept = np.polyfit(x, y, 1)
print(f"Equazione della retta di regressione: y = {slope}x + {intercept}")


# 4. Test Statistici

# Test t di Student (per due medie)
# Campione 1 e Campione 2
campione1 = np.array([10, 20, 30, 40, 50])
campione2 = np.array([15, 25, 35, 45, 55])

t_statistic, p_value = stats.ttest_ind(campione1, campione2)
print(f"Test t di Student - Statistica t: {t_statistic}, P-value: {p_value}")

# Test Chi-quadrato (per l'indipendenza)
# Dati di esempio (frequenze osservate ed attese)
osservato = np.array([10, 20, 30])
atteso = np.array([15, 25, 20])

chi2_statistic, p_value_chi2 = stats.chisquare(osservato, atteso)
print(f"Test Chi-quadrato - Statistica Chi2: {chi2_statistic}, P-value: {p_value_chi2}")
