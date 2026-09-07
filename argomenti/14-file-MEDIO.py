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
import csv
import json
lista_stringhe = []
#parte 1
with open("esempio.txt", "r") as g:
    numero_righe = 0
    for riga in g:       
        numero_righe += 1
    print(f"numero righe: {numero_righe}")
          
with open("esempio.txt", "r") as f:
    contenuto_esempio = f.read()
    variabile_output = f"numero parole: {len(contenuto_esempio)}\n"
    print(variabile_output)
    lista_stringhe.append(variabile_output)

with open("shirts.csv", "w" , newline="") as h:
  writer = csv.writer(h)
  writer.writerow(["ID", "Taglia","Colore", "Prezzo"])
  writer.writerow(["1234", "M","Verde", 20.40])
  writer.writerow(["3424","XL","Rosso", 23.10])
  writer.writerow(["3052", "S","Nero", 17.40])

#parte 2
somma_prezzo = 0
n_righe_cvs = 0  
with open("shirts.csv", "r") as r:
  reader = csv.DictReader(r)
  for riga_csv in reader:
      somma_prezzo += float(riga_csv["Prezzo"])
      n_righe_cvs += 1
      media_prezzo = somma_prezzo/n_righe_cvs
      prima_output = f"Magliette superiore alla media:\n"   
      if float(riga_csv["Prezzo"]) > media_prezzo:
        print(prima_output)
        lista_stringhe.append(prima_output)
        prima_output =    f"Taglia: {riga_csv["Taglia"], riga_csv["Colore"], riga_csv["Prezzo"]}\n"
        print(prima_output)
        lista_stringhe.append(prima_output)
  prima_output = f"La media del prezzo =  {media_prezzo}\n"
  print(prima_output)
  lista_stringhe.append(prima_output)

#parte 3

inventario ={
  "magliette": [
    {"taglia": "M", "quantita": 20},
    {"taglia": "L", "quantita": 40}
  ],
  "pantaloni": [
   {"taglia": "Ciccionis", "quantita": 13}
  ]
}
with open("inventory.json", "w") as l:
  json.dump(inventario, l, indent=4)

with open("inventory.json", "r") as m:
  dati = json.load(m)

  for key in list(dati.keys()):
    numero_tot = 0
    for elemento in dati[key] :
      numero_tot += elemento["quantita"]
    output_json = f"Categoria {key}: {numero_tot} prodotti\n"
    print(output_json) 
    lista_stringhe.append(output_json)
with open("report.txt", "w") as n:
   n.writelines(lista_stringhe)