#La funzione deve dividere a per b e restituire il risultato float. Se b è zero, deve restituire None e stampare "Errore: divisione per zero".
#Esempio: dividi(10,2) → 5.0, dividi(5,0) → None

def dividi(a, b):
    try:

        return a / b
    except ValueError:
        print("Errore: divisione per zero")
        return 0

print(dividi(10, 2))
print(dividi(5, 0))