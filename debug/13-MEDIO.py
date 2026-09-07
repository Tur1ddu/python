#Gestisci le spese giornaliere
spese = []
print("Registro Spese")
while True:
    voce = input("Cosa hai comprato? (o 'fine'): ")
    if voce == "fine":
        break
    prezzo = input("Quanto hai speso? ")
    spese.append(prezzo)

totale = 0
for spesa in spese:
    totale = totale + spesa

print(f"Hai speso un totale di: {totale:.2f}")