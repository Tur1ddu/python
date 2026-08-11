"""
Scrivi un programma Python che esegua le seguenti operazioni  utilizzando esclusivamente input da tastiera e output testuale:

1. Il programma deve chiedere all'utente di inserire tre valori:
   - un numero intero,
   - un numero decimale (float),
   - una stringa composta da almeno 5 caratteri.

2. Verifica che la stringa inserita abbia almeno 5 caratteri,
altrimenti richiedi nuovamente l'input fino a che la condizione è soddisfatta.

3. Calcola la somma del numero intero e del float, e assegna il risultato a una variabile.

4. Converte tale somma in una stringa e concatena la stringa inserita dall'utente, formando un'unica stringa.

5. Stampa:
   - il tipo di ogni variabile coinvolta (numero intero, numero decimale, stringa iniziale, somma calcolata,
   risultato della concatenazione)
   - la dimensione in byte di ciascuna di queste variabili (usando sys.getsizeof)
   - la lunghezza della stringa iniziale e della stringa risultante dalla concatenazione.

6. Infine, formatta l'output in modo leggibile, mostrando le informazioni raccolte
con attenzione alla precisione dei numeri float (con due cifre decimali).

Utilizza solo le funzioni input(), print(), float(), int(), str(), type(), len() e sys.getsizeof
importate dal modulo sys, e presta attenzione all’uso corretto del casting per evitare eccezioni.

Concentrati sulle variabili mutabili e immutabili, tipizzazione forte e casting esplicito, e formattazione dei dati numerici.

Ricorda:
input() ritorna sempre una stringa e che devi convertire gli input numerici al tipo corretto.
Ricontrolla che la concatenazione di stringhe avvenga solo dopo aver convertito correttamente i tipi numerici.

Esempio:

input:
42
3.1415
Python
output:
Intero inserito: 42 (tipo: <class 'int'>, dimensione: 28 byte)
Float inserito: 3.1415 (tipo: <class 'float'>, dimensione: 24 byte)
Stringa iniziale: Python (tipo: <class 'str'>, dimensione: 55 byte, lunghezza: 6)
Somma intero + float: 45.14 (tipo: <class 'float'>, dimensione: 24 byte)
Stringa concatenata: 45.14Python (tipo: <class 'str'>, dimensione: 72 byte, lunghezza: 12)

input:
10
2.718
Data

output:
La stringa inserita è troppo corta. Inserisci una stringa di almeno 5 caratteri.

input:
10
2.718
DataSci

output:
Intero inserito: 10 (tipo: <class 'int'>, dimensione: 28 byte)
Float inserito: 2.72 (tipo: <class 'float'>, dimensione: 24 byte)
Stringa iniziale: DataSci (tipo: <class 'str'>, dimensione: 62 byte, lunghezza: 7)
Somma intero + float: 12.72 (tipo: <class 'float'>, dimensione: 24 byte)
Stringa concatenata: 12.72DataSci (tipo: <class 'str'>, dimensione: 75 byte, lunghezza: 11)
"""

