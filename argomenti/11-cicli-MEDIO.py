"""

L'utente inserirà da tastiera una sequenza di numeri interi.
La sequenza termina quando l'utente digita la parola "fine".
I numeri inseriti devono essere salvati in una lista.

Dovrai quindi utilizzare un ciclo for per iterare sulla lista dei numeri inseriti e calcolare:

- la somma di tutti i numeri,
- il conteggio di quanti numeri sono maggiori di zero,
- il valore massimo tra i numeri.

Infine, dovrai stampare i risultati con una frase esplicativa.

Esempio:
input:
10
-3
25
0
100
fine

output:
Somma totale: 132
Numeri maggiori di zero: 3
Valore massimo: 100

input:
-1
-4
-2
-10
fine

output:
Somma totale: -17
Numeri maggiori di zero: 0
Valore massimo: -1

input:
5
20
15
20
5
fine

output:
Somma totale: 65
Numeri maggiori di zero: 5
Valore massimo: 20

"""
#parte 1
lista_numeri = []
while True:
    try:
        numero_input = input("inserire numero intero:\n")
        if numero_input == "fine":
            break
        numero_intero = int(numero_input)
        if numero_intero >= 0 or numero_intero < 0:
            lista_numeri.append(numero_intero)
        else:
            print("inserisci soltanto numeri interi maggiori o minori di 0")
    except ValueError:
        print("errore di sistema, questo non è un numero o non è un numero intero")
print(lista_numeri)

#parte 2
somma_numeri = 0
lista_n_maggiori = []
n_max = 0
for numero in lista_numeri:
    somma_numeri += numero
    if numero > n_max:
        n_max = numero
    if numero > 0:
        lista_n_maggiori.append(numero)
print(f"somma totale --> {somma_numeri}")
print(f"numeri maggiori di zero  --> {len(lista_n_maggiori)}")
print(f"numero massimo --> {n_max}")
print(lista_numeri)
