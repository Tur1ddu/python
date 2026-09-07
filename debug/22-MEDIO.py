# Risultato atteso:
#   La funzione "raggruppa_per" riceve una lista di dizionari
#   e il nome di una chiave, e restituisce un nuovo dizionario
#   in cui ogni valore distinto di quella chiave diventa la
#   chiave del gruppo, e il valore è la lista dei dizionari
#   con quel valore.
#   Esempio:
#       dati = [
#           {"nome": "Marco", "città": "Roma"},
#           {"nome": "Anna",  "città": "Milano"},
#           {"nome": "Luca",  "città": "Roma"},
#       ]
#       raggruppa_per(dati, "città") → {
#           "Roma":    [{"nome": "Marco", "città": "Roma"},
#                       {"nome": "Luca",  "città": "Roma"}],
#           "Milano":  [{"nome": "Anna",  "città": "Milano"}]
#       }

def raggruppa_per(lista, chiave):
    gruppi = {}
    for elemento in lista:
        valore = elemento[chiave]
        if valore not in gruppi:
            gruppi[valore] = {}
        gruppi[valore].append(elemento)
    return gruppi


dati = [
    {"nome": "Marco", "città": "Roma"},
    {"nome": "Anna",  "città": "Milano"},
    {"nome": "Luca",  "città": "Roma"},
    {"nome": "Sara",  "città": "Milano"},
]

risultato = raggruppa_per(dati, "città")
for città, persone in risultato.items():
    print(f"{città}: {[p['nome'] for p in persone]}")