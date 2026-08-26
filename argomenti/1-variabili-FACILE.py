"""
Scrivi un programma che:

1. Chieda all'utente di inserire il proprio nome (stringa).
2. Chieda all'utente di inserire la propria età (numero intero).
3. Chieda all'utente di inserire la propria altezza in metri (numero decimale, float).
4. Calcoli e stampi a schermo un messaggio formattato che includa:
   - Il nome inserito,
   - L'età,
   - L'altezza con due cifre decimali.

5. Calcoli l'anno di nascita approssimativo sottraendo l'età dall'anno corrente (puoi considerare l'anno 2024).
6. Stampi l'anno di nascita ottenuto.

Assicurati di convertire correttamente i tipi di dato ricevuti dall'input (stringhe) in numeri interi o float dove serve
e che il messaggio finale sia leggibile e chiaro.

Non sono richiesti controlli avanzati sugli input, ma dovrai utilizzare correttamente variabili, tipi di dati e casting.


Esempio:

input:
Anna
25
1.68

output:
Ciao Anna, hai 25 anni e sei alta 1.68 metri.
Sei nata approssimativamente nel 1999.

input:
Marco
40
1.75

output:
Ciao Marco, hai 40 anni e sei alta 1.75 metri.
Sei nato approssimativamente nel 1984.
"""
nome = input("inserire nome\n")
eta = int(input("inserire eta\n"))
altezza = float(input("inserire altezza\n"))
anno_nascita = 2026 - eta
print(f"Ciao {nome}, hai {eta} anni e sei alto {altezza} metri. \nSei nato approssimativamente nel {anno_nascita}.")