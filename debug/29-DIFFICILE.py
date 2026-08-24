# Risultato atteso:
#   La funzione deve trovare TUTTE le permutazioni di una stringa
#   e restituirle come lista di stringhe. L'ordine non importa,
#   ma non ci devono essere duplicati.
#   Esempio:
#       permutazioni("ab")  → ["ab", "ba"]
#       permutazioni("abc") → ["abc", "acb", "bac", "bca", "cab", "cba"]
#       permutazioni("a")   → ["a"]
#       permutazioni("")    → [""]

def permutazioni(stringa):
    if len(stringa) <= 1:
        return stringa

    risultato = []
    for i, carattere in enumerate(stringa):
        resto = stringa[:i] + stringa[i+1:]
        for perm in permutazioni(resto):
            risultato.append(perm + carattere)

    return risultato


print(permutazioni("ab"))
print(permutazioni("abc"))
print(permutazioni("a"))
