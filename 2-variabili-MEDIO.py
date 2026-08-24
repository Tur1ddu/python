"""
In questa esercitazione lavorerai con variabili di diversi tipi di dato,
eseguendo conversioni esplicite (casting),
operazioni aritmetiche e formattazione dell'output.
Dovrai leggere input dall'utente, conservarlo in variabili opportunamente tipizzate,
effettuare calcoli e mostrare risultati formattati.

In particolare, dovrai:
1. Leggere da tastiera il nome di una persona, la sua età (numero intero) e la sua altezza in metri (numero decimale).
2. Convertire e assegnare correttamente i valori inseriti alle variabili (attenzione: input() restituisce stringhe).
3. Calcolare l'anno di nascita assumendo che l'anno corrente sia 2024, sottraendo l'età.
4. Calcolare il peso ideale stimato con la formula: peso_ideale = altezza_in_metri * 25 (considera l'altezza come float).
5. Stampare tutte le informazioni raccolte e calcolate in modo leggibile e ordinato,
utilizzando vari tipi di formattazione, come f-string (se specifico), oppure format(), o l'operatore %.
6. Gestire eventuali errori semplici di conversione (ad esempio se l'età o l’altezza non sono convertibili nel tipo numerico richiesto, 
il programma deve terminare mostrando un messaggio significativo).

L'obiettivo è consolidare la gestione delle variabili,
delle conversioni tra tipi, e dell'input/output testuale,
approfondendo anche l’uso di funzioni come type(), int(), float(), str() e print() con formattazione.


Esempio:

input:
Mario Rossi
28
1.75

output:
Nome: Mario Rossi
Età: 28 anni
Altezza: 1.75 metri
Anno di nascita stimato: 1996
Peso ideale stimato (kg): 43.75

input:
Anna
venticinque
1.68

output:
Errore: l'età deve essere un numero intero valido.

input:
Luca
34
uno

output:
Errore: l'altezza deve essere un numero decimale valido.
"""
nome = input("inserire nome\n")
eta = int(input("inserire eta\n"))
altezza = float(input("inserire altezza\n"))
anno_nascita = 2025 - eta
peso_ideale = altezza * 25
print(f"Nome: {nome} \nEtà: {eta} anni \nAltezza: {altezza} \nAnno di nascita stimato:{anno_nascita} \nPeso ideale stimato (kg): {peso_ideale}")