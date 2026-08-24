"""
Realizza un programma che svolge le seguenti operazioni su file:

1) File di testo (.txt):
- Apri un file di testo fornito (es. "frasi.txt") in modalità lettura con codifica UTF-8.
- Leggi tutte le righe e memorizzale in una lista.
- Per ogni riga, conta il numero delle parole (considera una parola come una sequenza di caratteri separati da spazi).
- Crea un nuovo file di testo (es. "frasi_count.txt") dove ad ogni riga del file originale viene aggiunto, tra parentesi, il numero di parole presenti.
- Gestisci eventuali eccezioni dovute alla mancanza del file o problemi di lettura.

2) File CSV:
- Leggi un file CSV (es. "prodotti.csv") che contiene le colonne: "id", "nome", "categoria", "prezzo".
- Usa csv.reader e csv.DictReader per caricare i dati, distinguendo intestazione da righe dati.
- Calcola:
   a) il numero totale di prodotti.
   b) il prezzo medio dei prodotti.
   c) la categoria con il maggior numero di prodotti.
- Scrivi in un nuovo file CSV (es. "prodotti_filtrati.csv") solo i prodotti con prezzo superiore alla media.
- Cura la gestione del carattere di nuova riga nel file di output per evitare righe vuote.

3) File JSON:
- Carica un file JSON (es. "magazzino.json") che rappresenta un inventario con varie categorie e liste di prodotti.
- Estrai la lista di prodotti di una categoria specifica scelta dall'utente (input da tastiera).
- Calcola il valore totale (somma dei prezzi) per quella categoria e stampa su schermo.
- Aggiorna il JSON aggiungendo un campo 'disponibile: true/false' per ogni prodotto in base a una condizione stabilita dal programma (es. prezzo minore di un valore fisso).
- Salva il JSON modificato in un nuovo file (es. "magazzino_aggiornato.json") con formattazione leggibile (indentato).
- Gestisci eventuali errori nella lettura dei file o input errati.

Esempio:

input:
magazzino.json contiene:
{
  "magliette": [{"nome": "Vintage", "prezzo": 10}, {"nome": "Sport", "prezzo": 15}],
  "pantaloni": [{"nome": "Jeans", "prezzo": 20}, {"nome": "Cargo", "prezzo": 30}]
}

categoria richiesta:
magliette

output:
Valore totale prodotti nella categoria 'magliette': 25

Questo genera anche un file magazzino_aggiornato.json con campo "disponibile": true per prodotti con prezzo < 20.

---

input:
prodotti.csv contiene:
id,nome,categoria,prezzo
1,T-Shirt,Casual,12.5
2,Jeans,Casual,35
3,Sneakers,Sport,50

output:
Numero totale prodotti: 3
Prezzo medio: 32.5
Categoria più numerosa: Casual

Il file prodotti_filtrati.csv conterrà prodotto 2 e 3 perchè prezzo > 32.5

---

input:
frasi.txt contiene:
Ciao mondo
Programmare in Python è bello

output:
frasi_count.txt contiene:
Ciao mondo (2)
Programmare in Python è bello (5)

"""