#La funzione deve restituire un dizionario con ogni parola e il numero di volte in cui appare nella lista.
#Esempio: conta_parole(["a","b","a"]) → {"a":2, "b":1}

def fattoriale(n):
    if n == 1:
        return 1
    return n * fattoriale(n)

print(fattoriale(5))
print(fattoriale(0))