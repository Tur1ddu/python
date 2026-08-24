"""
classificazione di un numero
- Chiedi all'utente di inserire un numero intero mediante input()
- Controlla se il numero è positivo, negativo o zero
- Inoltre verifica se il numero è pari o dispari
- stampare messaggi appropriati, ad esempio "Il numero è positivo e pari", "Il numero è negativo e dispari", o "Il numero è zero"

"""
intero = int(input("inserisci un numero intero"))



if intero < 0 :
    print("numero è minore a 0 (negativo)")
elif intero > 0 :
    print("numero è maggiore a 0 (positivo)")
elif intero == 0:
    print("numero è 0")

if intero % 2 == 0:
    print("ed è un numero è pari")
else:
    print("ed è un numero è pari")