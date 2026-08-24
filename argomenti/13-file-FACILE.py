"""
Scrivi un programma che:

1) Legge il contenuto di un file di testo chiamato "proverbio.txt".
   - Usa la funzione open() con modalità di lettura.
   - Leggi tutto il contenuto usando il metodo read() e poi chiudi il file.

2) Mostra il contenuto letto stampandolo a schermo.

3) Apre (o crea se non esiste) un file di testo chiamato "output.txt" in modalità scrittura ('w').
   - Scrive sul file due righe separate:
     - La prima riga deve essere "Contenuto originale:" seguita dal contenuto letto dal file "proverbio.txt".
     - La seconda riga deve essere "Numero di caratteri: " seguito dal numero totale di caratteri del testo letto.
   - Chiudi il file dopo la scrittura.

Esempio:

input:
(Il file proverbio.txt contiene: "Chi va piano va sano e va lontano")

output:
Chi va piano va sano e va lontano

// Il file output.txt creato contiene:
Contenuto originale: Chi va piano va sano e va lontano
Numero di caratteri: 34

input:
(Il file proverbio.txt contiene: "Meglio un uovo oggi che una gallina domani")

output:
Meglio un uovo oggi che una gallina domani

// Il file output.txt creato contiene:
Contenuto originale: Meglio un uovo oggi che una gallina domani
Numero di caratteri: 42

"""


with open("proverbio.txt","r") as f:
   fileProverbio = f.read()
   print(fileProverbio)
   #chiude in automatico with


with open("output.txt","w") as f:
   f.write(f"Contenuto originale: {fileProverbio}")
   f.write(f"numero di caratteri: {len(fileProverbio)}")


with open("output.txt","w+") as f:
   f.write(f"Contenuto originale: {fileProverbio}")
   f.write(f"numero di caratteri: {len(fileProverbio)}")

#la w+ soprascrive ma se il file non esiste non funziona