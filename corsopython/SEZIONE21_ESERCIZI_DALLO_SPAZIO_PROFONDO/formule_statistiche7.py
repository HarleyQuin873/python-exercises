import numpy as np
import scipy.stats as stats

# Dati di esempio
dati = np.array([10,20,30,40,50])

# 1. Statistiche descrittive
#Le statistiche descrittive servono per sintetizzare e descrivere le caratteristiche principali di un insieme di dati.

#Media
#La media è la somma di tutti i valori divisa per il numero totale di osservazioni. È una misura di tendenza centrale ed è utilizzata quando i dati sono distribuiti in modo relativamente uniforme.
media = np.mean(dati)

#Mediana
#La mediana è il valore che si trova nel mezzo di un set di dati ordinato. È una misura di tendenza centrale che è meno influenzata dai valori estremi rispetto alla media, quindi utile quando i dati sono asimmetrici o contengono outliers.
mediana = np.median(dati)

#Moda
#La moda è il valore che appare più frequentemente in un insieme di dati. Non tutti i dataset hanno una moda, e può esserci più di una moda se ci sono più valori con la stessa frequenza.
moda_result = stats.mode(dati)
# moda = moda_result.mode if isinstance(moda_result.mode, np.ndarray) and len(moda_result.mode) > 0
# else None
moda = moda_result.mode if isinstance(moda_result.mode, np.ndarray) and len(moda_result.mode) > 0 else None
#e moda_result.mode è un array numpy (un np.ndarray) e contiene almeno un elemento, allora restituiamo la moda.
# Altrimenti, restituiamo None, che significa che non c'è una moda definita (ad esempio, se non c'è un elemento che si ripete più volte, quindi non c'è una moda).
# isinstance(moda_result.mode, np.ndarray): verifica se moda_result.mode è un array numpy. Questo è utile perché stats.mode() potrebbe restituire un array anche se c'è una sola moda, quindi dobbiamo verificare che l'oggetto sia effettivamente un array numpy.

# len(moda_result.mode) > 0: questa parte verifica che l'array moda_result.mode abbia almeno un elemento. Questo è utile per evitare di assegnare un valore vuoto se non esistono mode (ad esempio, se tutte le osservazioni sono uniche, non c'è una moda).

#Varianza
# La varianza misura la dispersione dei dati rispetto alla loro media. È il quadrato della deviazione standard e viene utilizzata per capire quanto i dati siano sparsi. Più alta è la varianza, maggiore è la dispersione dei dati.
varianza = np.var(dati)

#Deviazione standard
#La deviazione standard è la radice quadrata della varianza. È un'indicazione di quanto i dati siano dispersi attorno alla media. Una bassa deviazione standard indica che i dati sono concentrati vicino alla media.
deviazione_standard = np.std(dati)

#Range
#Il range è la differenza tra il valore massimo e il valore minimo dei dati. È una misura di dispersione che fornisce una stima della "larghezza" del dataset.
range_dati = np.max(dati) - np.min(dati)

#Risultati delle statistiche descrittive
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Varianza: {varianza}")
print(f"Deviazione standard: {deviazione_standard}")
print(f"Range: {range_dati}")

# 2. Statistiche Inferenziali
#Le statistiche inferenziali si usano per fare inferenze su una popolazione a partire da un campione di dati. Questo processo coinvolge anche l'uso di test di ipotesi e intervalli di confidenza.


# Z-Score (per un valore specifico, ad esempio 30)
#Il Z-score misura quanto un dato è distante dalla media in termini di deviazioni standard. Un z-score positivo indica che il valore è sopra la media, mentre uno negativo indica che è sotto. Il calcolo dello Z-score è utile per capire quanto un dato sia "strano" rispetto alla distribuzione.
z_score = (30 - media) / deviazione_standard
print(f"Z-Score per 30: {z_score}")


#Intervallo di confidenza (ad esempio il 95%)
#Un intervallo di confidenza è un range di valori che stima un parametro della popolazione (come la media) con un certo livello di fiducia. Ad esempio, un intervallo di confidenza al 95% significa che, se ripetessimo l'esperimento molte volte, l'intervallo contenerebbe la vera media 95 volte su 100.
confidence_level = 0.95
z_value = stats.norm.ppf((1 + confidence_level) / 2) # valore critico per un intervallo di confidenza di 95%
errore_standard = deviazione_standard / np.sqrt(len(dati))
intervallo_confidenza = (media - z_value * errore_standard, media + z_value * errore_standard) 
print(f"Intervallo di confidenza al 95%: {intervallo_confidenza}")
#confidence_level: Il livello di confidenza è la probabilità che un intervallo di confidenza contenga il parametro vero della popolazione (ad esempio, la media). È un valore tra 0 e 1. Ad esempio, un livello di confidenza del 95% corrisponde a confidence_level = 0.95.

# (1 + confidence_level) / 2: Questa parte calcola il valore che rappresenta la probabilità cumulata da una delle estremità della distribuzione normale, che deve essere uguale alla metà del livello di confidenza.

# stats.norm.ppf(...): La funzione ppf (percent point function) è l'inverso della funzione di distribuzione cumulativa (CDF) della distribuzione normale. ppf(p) restituisce il valore z tale che la probabilità cumulata fino a z sia pari a p. In altre parole, dato un valore di probabilità p, ppf(p) restituisce il valore z che separa la probabilità p dalla coda di sinistra della distribuzione normale.



# 3. Correlazione e regressione
#Le analisi di correlazione e regressione servono a esplorare la relazione tra due variabili.

# Dati di esempio (due variabili)
x = np.array([1,2,3,4,5])
y = np.array([2,4,5,4,5])

# Coefficiente di correlazione di Pearson
#Il coefficiente di correlazione di Pearson misura la forza e la direzione di una relazione lineare tra due variabili. Un valore di 1 indica una correlazione positiva perfetta, -1 una correlazione negativa perfetta e 0 nessuna correlazione.
correlazione = np.corrcoef(x, y)[0, 1]
print(f"Coefficiente di correlazione di Pearson: {correlazione}")

#Regressione lineare (usiamo la funzione polyfit di numpy)
#La regressione lineare cerca di trovare la retta che meglio approssima la relazione tra due variabili. La formula della retta è y = mx + b, dove m è la pendenza (coefficiente angolare) e b è l'intercetta con l'asse delle ordinate. È utile per predire il valore di una variabile in base a un'altra.
slope, intercept = np.polyfit(x, y, 1)
print(f"Equazione della retta di regressione: y = {slope}x + {intercept}")

# 4. Test Statistici
#I test statistici sono utilizzati per testare ipotesi riguardo a una popolazione sulla base di un campione.

# test t di Student (per due medie)
#Il test t di Student confronta due medie di campioni indipendenti per vedere se esiste una differenza significativa tra di esse. La statistica t indica la distanza tra le medie, mentre il p-value fornisce la probabilità che la differenza osservata sia dovuta al caso. Se il p-value è inferiore a un valore di soglia (ad esempio 0,05), si può rifiutare l'ipotesi nulla (che le medie siano uguali).
#Quando esegui un test t di Student, l'ipotesi nulla (H₀) di solito afferma che le medie dei due gruppi sono uguali. L'ipotesi alternativa (H₁) invece sostiene che le medie dei due gruppi siano diverse.

# Interpretazione del p-value:
# Se il p-value è basso (ad esempio, inferiore a 0,05), significa che la probabilità che la differenza tra le medie osservate sia dovuta al caso è molto bassa. In altre parole, è improbabile che la differenza osservata sia casuale, quindi rifiutiamo l'ipotesi nulla e concludiamo che c'è una differenza significativa tra le due medie.
# Se il p-value è alto (maggiore di 0,05), non possiamo rifiutare l'ipotesi nulla, il che significa che non c'è abbastanza evidenza per dire che le medie siano diverse. In questo caso, la differenza tra le medie potrebbe essere dovuta al caso, quindi non possiamo affermare che ci sia una differenza significativa.
# In sintesi:
# Rifiutiamo l'ipotesi nulla se il p-value è basso (meno di 0,05). Questo indica che la differenza osservata è significativa e probabilmente non dovuta al caso.
# Non rifiutiamo l'ipotesi nulla se il p-value è alto (maggiore di 0,05). In questo caso, la differenza potrebbe essere dovuta al caso, quindi non possiamo concludere che le medie siano diverse.
# In breve:
# Se il p-value è basso, rifiutiamo l'ipotesi nulla e concludiamo che la differenza tra le medie non è casuale. Se il p-value è alto, non possiamo rifiutare l'ipotesi nulla e la differenza potrebbe essere dovuta al caso.
#Campione 1 e campione 2
campione1 = np.array([10,20,30,40,50])
campione2 = np.array([15,25,35,45,55])

t_statistic, p_value = stats.ttest_ind(campione1, campione2)
print(f"Test t di Student - Statistica t: {t_statistic}, P-value: {p_value}")

#Test Chi-quadro 
#Il test Chi-quadro è utilizzato per confrontare le frequenze osservate con quelle attese per determinare se esiste una discrepanza significativa tra di esse. Viene spesso utilizzato per analizzare le distribuzioni di frequenza di variabili categoriche.

# Dati di esempio ( frequenze osservate ed attese)
osservato = np.array([10, 20, 30])
atteso = np.array([15, 25, 20])

chi2_statistic, p_value_chi2 = stats.chisquare(osservato, atteso)
print(f"Test Chi-quadro - Statistica Chi2: {chi2_statistic}, P-value: {p_value_chi2}")




#In sintesi:
# Le statistiche descrittive offrono un quadro generale dei dati (media, varianza, etc.).
# Le statistiche inferenziali ci permettono di fare inferenze sulla popolazione a partire da un campione, come con gli intervalli di confidenza e gli Z-score.
# Le analisi di correlazione e regressione esplorano le relazioni tra variabili.
# I test statistici (come il test t di Student e il test Chi-quadro) sono utilizzati per testare ipotesi su campioni o popolazioni.