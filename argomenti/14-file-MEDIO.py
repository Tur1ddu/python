"""
Dovrai realizzare un piccolo programma che:

1. Legga un file di testo (file.txt) e conti quante righe ci sono e quante parole contiene in totale.

2. Legga un file CSV (shirts.csv) contenente un elenco di magliette con colonne:
id, taglia, colore, prezzo.
Il programma dovrà calcolare la media del prezzo delle magliette e stampare tutte quelle con prezzo superiore alla media,
formattando l'output indicando taglia, colore e prezzo.

3. Legga un file JSON (inventory.json) che rappresenta un magazzino con categorie di prodotti (es. magliette, pantaloni)
e per ogni categoria una lista di prodotti con taglia e quantità.
Il programma deve stampare per ogni categoria il numero totale di prodotti (sommando le quantità) presenti.

4. Scriva su un nuovo file di testo (report.txt) un breve report che riassuma i risultati ottenuti dalle letture precedenti,
evidenziando numero di righe e parole del testo, media dei prezzi e magliette sopra la media, e i totali delle categorie del JSON.


Esempio:
input: contenuto di file.txt:
Ciao mondo
Questo è un file di esempio.
Contiene alcune righe di testo.

output atteso nel console:
Numero righe: 3
Numero parole: 13

input: contenuto di shirts.csv:
id,taglia,colore,prezzo
1,M,rosso,15.5
2,L,blu,20.0
3,S,verde,12.0
4,M,nero,25.0
5,L,rosso,18.0

output atteso nel console:
Prezzo medio: 18.1
Magliette con prezzo superiore alla media:
- Taglia: L, Colore: blu, Prezzo: 20.0
- Taglia: M, Colore: nero, Prezzo: 25.0

input: contenuto di inventory.json:
{
  "magliette": [
    {"taglia": "M", "quantita": 10},
    {"taglia": "L", "quantita": 5}
  ],
  "pantaloni": [
    {"taglia": "XL", "quantita": 7}
  ]
}

output atteso nel console:
Categoria magliette: 15 prodotti
Categoria pantaloni: 7 prodotti

output atteso in report.txt:
Numero righe del file di testo: 3
Numero parole nel file di testo: 13
Prezzo medio magliette: 18.1
Magliette sopra la media:
  - Taglia L, colore blu, prezzo 20.0
  - Taglia M, colore nero, prezzo 25.0
Totali per categoria magazzino:
  magliette: 15
  pantaloni: 7

"""