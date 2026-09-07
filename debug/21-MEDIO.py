#Rinominare un file per simularne il backup
import os

file_originale = "dati.csv"
if os.path.exists(file_originale):
    os.rename(file_originale, "backup/dati_vecchi.csv")
    print("Backup completato")
else:
    print("Errore: il file non esiste")