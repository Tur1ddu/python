"""
Scrivi un programma che:

1. Chieda all'utente di inserire una lista di numeri interi positivi da tastiera.
Puoi farlo ripetendo la lettura di un numero finché l'utente non inserisce la stringa "stop".

2. Una volta terminato l'inserimento, il programma deve calcolare e stampare:
  - la somma di tutti i numeri inseriti
  - la media aritmetica dei numeri inseriti
  - il numero massimo tra quelli inseriti

Nel caso in cui non venga inserito alcun numero (l'utente inserisca subito "stop"),
dovrai stampare un messaggio che indica che non ci sono numeri su cui calcolare i risultati.

Usa un ciclo while o for per gestire l'inserimento multiplo e per i calcoli (come sommare o trovare il massimo)
puoi usare variabili che aggiorni ad ogni iterazione.

Stampa i risultati con messaggi chiari e valori numerici appropriati.

Esempio:
input:
10
20
5
stop

output:
Somma: 35
Media: 11.666666666666666
Massimo: 20

input:
stop

output:
Nessun numero inserito, impossibile calcolare somma, media e massimo.
"""
#parte 

lista_numeri = []
while True:
  try:
    numero_utente = input("inserire numero:\n")
    if numero_utente == "stop":
      break
    numero_positivo = int(numero_utente)
    if numero_positivo > 0:
      lista_numeri.append(numero_positivo)
    else:
      print("inserisci solo numeri positivi")
  except ValueError:
    print("errore di sistema, questo non è un numero") 
print(lista_numeri)

#parte 2
somma_numeri = 0
n_max = 0
for numero in lista_numeri :
    somma_numeri += numero
    if numero > n_max:
      n_max = numero
media_artmetica = somma_numeri/len(lista_numeri)
print(f"la media artimetica è --> {media_artmetica}")
print(f"la sommma dei numeri è --> {somma_numeri}")
print(f"numero massimo --> {n_max}")
print(lista_numeri)