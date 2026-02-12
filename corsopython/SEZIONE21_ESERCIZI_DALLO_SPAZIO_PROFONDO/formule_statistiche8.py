import numpy as np
import scipy.stats as stats

#Dati di esempio
dati = np.array([10,20,30,40,50])

# 1.Statistiche descrittive
# Le statistiche descrittive servono per descrivere e sintetizzare le caratteristiche principali di un insieme di dati.

#Media
#La media è la somma di tutti i valori divisa per il totale di osservazioni. E' una misura di tendenza centrale e viene usata quando i dati sono distribuiti in modo relativamente uniforme.
media = np.mean(dati)

#Mediana
#La mediana è il valore che si trova nel mezzo di un set di dati ordinato. E' una misura di tendenza centrale che è meno influenzata dai valori estremi rispetto alla media. E' utilizzata nel caso di valori molto asimmetrici o in caso di presenza di outliers.
mediana = np.median(dati)

#Moda
#La moda è il valore che appare più frequentemente in un insieme di dati. Non tutti i dataset hanno una moda e può esserci più di una moda nel caso di siano più valori con la stessa frequenza.
moda_result = stats.mode(dati)
moda = moda_result.mode if isinstance(moda_result.mode, np.ndarray) and len(moda_result.mode) > 0 else None

#Varianza
#La varianza misura la dispersione dei dati rispetto alla loro media. E' il quadrato della deviazione standard e viene usata per capire quanto i dati siano sparsi. Più è alta la varianza, maggiore è la dispersione dei dati.
varianza = np.var(dati)

#Deviazione standard
#La deviazione standard è la radice quadrata della varianza. Indica quanto i dati siano dispersi lontano dalla media. Una bassa deviazione standard indica che i dati sono concentrati vicino alla media. E' più comoda rispetto alla varianza perchè la varianza è espressa in potenze elevate al quadrato, mentre la deviazione standard no.
deviazione_standard = np.std(dati)

#Range
#Il range indica l'ampiezza dell'intervallo dei valori del dataset perchè misura la differenza tra il valore massimo ed il valore minimo, quindi è una misura di dispersione dei dati.
range_dati = np.max(dati) - np.min(dati)

#Risultati delle statistiche descrittive
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Varianza: {varianza}")
print(f"Deviazione standard: {deviazione_standard}")
print(f"Range: {range_dati}")

# 2. Statistiche inferenziali
#Le statistiche inferenziali si usano per fare inferenze su una popolazione a partire da un campione di dati. Questo processo coinvolge anche test di ipotesi e intervalli di confidenza.

#Z-Score (per un valore specifico, ad esempio 30)
#Il Z-Score misura quanto un dato sia distante dalla media in termini di deviazione standard. Uno Z-score positivo indica che il valore è sopra la media, metre un valore negativo indica che è sotto. il calcolo dello Z-score è utile per capire quanto un valore sia "strano" rispetto alla DISTRIBUZIONE.
z_score = (30 - media) / deviazione_standard
print(f"Z-score: {z_score}")

#Intervallo di confidenza (ad esempio il 95%)
# Un intervallo di confidenza è un range di valori che stima un parametro della popolazione( ad esempio la media) con un certo livello di fiducia. Ad esempio, un intervallo di confidenza al 95% indica che se ripetessimo l'esperimento 100 volte, 95 volte su 100, l'intervallo conterrebbe la media 95 volte su cento.
confidence_level = 0.95
z_value = stats.norm.ppf((1+ confidence_level) / 2)
errore_standard = deviazione_standard / np.sqrt(len(dati))
intervallo_confidenza = (media - z_value * errore_standard, media + z_value * errore_standard)
print(f"Intervallo di confidenza al 95%: {intervallo_confidenza}")

#Correlazione e regressione
#le analisi di correlazione e regressione servono per stabilire se vi è una relazione tra due variabili.

#Dati di esempio (due variabili)
x = np.array([1,2,3,4,5])
y = np.array([2,4,5,4,5])

#Coefficiente di correlazione di Pearson
#Il coefficiente di correlazione di Pearson misura la forza e la direzione di una relazione tra due variabili. Il valore 1 indica una correlazione positiva perfetta, il valore -1 indica una correlazione negativa perfetta, 0 indica nessuna correlazione.
correlazione = np.corrcoef(x,y)[0,1]
print(f"Coefficiente di correlazione di Pearson: {correlazione}")

#Regressione lineare
#Regressione lineare (usiamo la funzione polyfit di numpy)
#La regressione lineare cerca di trovare la retta che meglio approssima la relazione tra due variabili. La formula della retta é y= mx + C dove m è il coefficiente angolare e C è l'intercetta con l'asse delle ordinate. E' utile per predire il valore di una variabile in base ad un'altra.
slope, intercept = np.polyfit(x,y,1)
print(f"Equazione della retta di regressione: y = {slope}x + {intercept}")

# 4. Test statistici
#I test statistici sono usati per testare IPOTESI riguardo a una popolazione SULLA BASE DI UN Campione

#TEST T DI STUDENT (PER DUE MEDIE)
#Il test di student confronta due medie di campioni indipendenti per stabilire se vi sia una DIFFERENZA SIGNIFICATIVA TRA DI ESSE. La statistica t indica la DISTANZA tra le medie, mentre il p-value indica la probabilità che la DIFFERENZA OSSERVATA sia dovuta al caso. Se il p-value è inferiore a una soglia (0.05), si può rifiutare l'ipotesi nulla( che le medie siano uguali), quindi le il p-value è basso, la differenza è significativa, quindi non è dovuta al caso, se il p-value è alto, non possiamo rifiutare l'ipotesi nulla, quindi la probabilità che la differenza sia dovuta al caso è alta.
campione1 = np.array([10,20,30,40,50])
campione2 = np.array([15,25,35,45,55])

t_statistic, p_value = stats.ttest_ind(campione1, campione2)
print(f"Test T di Student - Statistica T: {t_statistic}, P-Value: {p_value}")

#Test Chi-quadro
#Il test del Chi quadro è utilizzato per CONFRONTARE le frequenze osservate con quelle attese PER DETERMINARE SE ESISTE UNA DISCREPANZA significativa tra di esse. Viene spesso utilizzato per analizzare le DISTRIBUZIONI DI FREQUENZA DI VARIABILI categoriche

#Dati di esempio
osservato = np.array([10, 20, 30])
atteso = np.array([15, 25, 20])

chi2_statistic, p_value_chi2 = stats.chisquare(osservato, atteso)
print(f"Test del CHI-QUADRO - Statistica-CHI2: {chi2_statistic}, P-Value: {p_value_chi2}")




