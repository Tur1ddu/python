"""
classificazione di un numero
- Chiedi all'utente di inserire un numero intero mediante input()
- Controlla se il numero è positivo, negativo o zero
- Inoltre verifica se il numero è pari o dispari
- stampare messaggi appropriati, ad esempio "Il numero è positivo e pari", "Il numero è negativo e dispari", o "Il numero è zero"

"""
numero = int(input("inserire numero intero\n"))

if numero == 0:
    print ("il numero è zero")
elif numero < 0 and numero %2 == 0:
    print ("il numero è negativo e pari")
elif numero < 0 and numero %2 != 0:
    print ("il numero è negativo e dispari")
elif numero > 0 and numero %2 == 0:
    print("il numero è positivo e pari")
else:
    print("il numero è positivo e dipari")