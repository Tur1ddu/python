#La funzione deve convertire gradi Celsius in Fahrenheit.
#Formula: (C × 9/5) + 32. Esempio: celsius_to_fahrenheit(0) → 32.0, celsius_to_fahrenheit(100) → 212.0

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))