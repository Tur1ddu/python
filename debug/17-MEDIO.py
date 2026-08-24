#La funzione deve restituire una lista piatta da una lista annidata a qualsiasi profondità.
#Esempio: appiattisci([1,[2,[3,4]],5]) → [1,2,3,4,5]

def appiattisci(lista):
    risultato = []
    for el in lista:
        if isinstance(el, list):
            risultato.append(appiattisci(el))
        else:
            risultato.append(el)
    return risultato

print(appiattisci([1,[2,[3,4]],5]))