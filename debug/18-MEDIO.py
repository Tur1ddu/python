#Il generatore deve produrre i primi n numeri di Fibonacci. Esempio: list(fibonacci(6)) → [0,1,1,2,3,5]

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a = b
        b = a + b

print(list(fibonacci(6)))