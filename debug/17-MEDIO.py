#Leggere un file di testo e contare quante volte appare una parola
def conta_errori(nome_file, parola):
    with open(nome_file, "w") as f:
        contenuto = f.read()
        conteggio = contenuto.count(parola)
    return conteggio

print(f"Errori trovati: {conta_errori('log.txt','ERROR')}")
print(f"Errori trovati: {conta_errori('log.txt','INFO')}")