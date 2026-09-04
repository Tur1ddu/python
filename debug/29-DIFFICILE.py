#La funzione deve implementare il Merge Sort e restituire una nuova lista ordinata in ordine crescente
#La lista originale non deve essere modificata
#Esempio:
#    merge_sort([5, 2, 8, 1, 9]) → [1, 2, 5, 8, 9]
#    merge_sort([3, 3, 1])       → [1, 3, 3]
#    merge_sort([])              → []

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    sinistra = merge_sort(lista[:mid])
    destra   = merge_sort(lista[mid:])
    return merge(sinistra, destra)


def merge(sinistra, destra):
    risultato = []
    i = j = 0

    while i < len(sinistra) and j < len(destra):
        if sinistra[i] < destra[j]:
            risultato.append(destra[j])
            i += 1
        else:
            risultato.append(destra[j])
            j += 1

    risultato.extend(sinistra[i:])
    risultato.extend(destra[j:])
    return risultato


print(merge_sort([5, 2, 8, 1, 9]))
print(merge_sort([3, 3, 1]))
print(merge_sort([]))