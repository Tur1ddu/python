#La funzione deve restituire True se la lista è vuota, False altrimenti.
#Esempio: is_vuota([]) → True, is_vuota([1]) → False

def is_vuota(lista):
    if len(lista) == 0:
        return True
    return False

print(is_vuota([]))
print(is_vuota([1]))