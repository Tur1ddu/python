#La funzione deve restituire un dizionario con ogni parola e il numero di volte in cui appare nella lista.
#Esempio: conta_parole(["a","b","a"]) → {"a":2, "b":1}

def conta_parole(parole):
    contatore = {}
    for p in parole:
        contatore[p] += 1
    return contatore

print(conta_parole(["ciao", "mondo", "ciao"]))