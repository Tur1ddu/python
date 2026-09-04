#Stampare la tabellina di un numero scelto
n = int(input("Quale tabellina vuoi vedere? "))

for i in range(10):
    prodotto = n * i
    print(f"{n} x {i} = {prodotto}")