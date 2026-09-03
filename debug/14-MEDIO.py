#La funzione deve dividere a per b e restituire il risultato float. Se b è zero, deve restituire None e stampare "Errore: divisione per zero".
#Esempio: dividi(10,2) → 5.0, dividi(5,0) → None

def filtra_pari(numeri):
    return [n for n in numeri if n % 2 != 0]

print(filtra_pari([1,2,3,4,5,6]))
