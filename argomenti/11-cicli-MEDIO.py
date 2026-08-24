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
number_major = 0

numeri = []

while True:
  scelta = input("Inserisci un numero (o scrivi 'stop' per finire): ")

  if scelta == "fine":
    break
  try:
    numero = int(scelta)
    if numero > 0 :
      number_major+=1
    numeri.append(numero)
  except ValueError:
    print("Errore: devi inserire un numero intero, non lettere o simboli a caso.")

if len(numeri) > 0:
  somma = sum(numeri)
  massimo = max(numeri)
  
  print(f"\nSomma: {somma}")
  print(f"Numeri maggiori di zero: {number_major}")
  print(f"Massimo: {massimo}")
else:
  print("\nNessun numero inserito, impossibile calcolare somma, media e massimo.")