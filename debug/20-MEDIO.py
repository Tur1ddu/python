#Salvare nomi ed email in un file CSV
import csv

def salva_contatto(nome, email):
    with open("contatti.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(nome, email)

salva_contatto("Mario", "mario@email.it")