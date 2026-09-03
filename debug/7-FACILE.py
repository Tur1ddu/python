#La funzione deve restituire il numero più grande tra i tre passati. Esempio: massimo(3, 9, 5) → 9

def massimo(a, b, c):
    max = 0  
    for maximo in [a, b, c]:
        if maximo > max:
             max = maximo
    return max # Questo va bene, ma riscrivi senza usare una lista

print(massimo(3, 9, 5))