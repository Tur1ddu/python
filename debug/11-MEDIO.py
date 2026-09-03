#Stampa i numeri da 1 a 20. Al posto dei multipli di 3 stampa "Fizz", di 5 stampa "Buzz", di entrambi stampa "FizzBuzz".

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0: 
        print("Fizz")
    else:
        print(i)