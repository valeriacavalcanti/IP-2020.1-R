def fibonacci(termo):
    a, b = 1, 0
    for i in range(termo - 1):
        a, b = b, a + b
    return b

def fibonacci_recursiva(termo):
    if termo == 1:
        return 0
    elif termo == 2:
        return 1
    else:
        return fibonacci_recursiva(termo - 1) + fibonacci_recursiva(termo - 2)

# PP

for i in range(1, 11):
    print(i, fibonacci(i))
    print(i, fibonacci_recursiva(i))
