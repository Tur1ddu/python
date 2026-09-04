#La funzione deve trovare l'indice di target in una lista ordinata usando la ricerca binaria, o -1 se non trovato.
#Esempio: ricerca_binaria([1,3,5,7,9], 5) → 2
#Esempio: ricerca_binaria([1,3,5,7,9], 6) → -1

def ricerca_binaria(lista, target):
    sx, dx = 0, len(lista)
    while sx <= dx:
        mid = (sx + dx) // 2
        if lista[mid] == target:
            return mid
        elif lista[mid] < target:
            sx = mid - 1
        else:
            dx = mid + 1
    return -1