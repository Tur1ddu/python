# Risultato atteso:
#   La funzione deve leggere una stringa in formato CSV
#   (valori separati da virgola, righe separate da "\n"),
#   ignorare la riga di intestazione e restituire una lista
#   di dizionari, uno per ogni riga dati.
#   Le chiavi del dizionario vengono dalla prima riga (intestazione).
#   Esempio:
#       csv = "nome,età,città\nMarco,30,Roma\nAnna,25,Milano"
#       parse_csv(csv) → [
#           {"nome": "Marco", "età": "30", "città": "Roma"},
#           {"nome": "Anna",  "età": "25", "città": "Milano"}
#       ]

def parse_csv(testo):
    righe = testo.split("\n")
    intestazione = righe[0].split(",")
    risultato = []

    for riga in righe:
        valori = riga.split(",")
        record = {}
        for i in range(len(intestazione)):
            record[intestazione[i]] = valori[i]
        risultato.append(record)

    return risultato


csv = "nome,età,città\nMarco,30,Roma\nAnna,25,Milano"
for r in parse_csv(csv):
    print(r)
