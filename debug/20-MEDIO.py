#Gestisci un set di nomi per evitare duplicati
studenti_presenti = {"Marco", "Anna"}
nuovo_studente = input("Chi è arrivato? ")

if nuovo_studente in studenti_presenti:
    print("Studente già registrato!")
else:
    studenti_presenti.add[nuovo_studente]
    print(f"Benvenuto {nuovo_studente}")

print("Totale presenti: " + len(studenti_presenti))