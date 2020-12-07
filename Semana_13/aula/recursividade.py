def foo(n):
    if n > 1:
        return n * foo(n - 1)
    return n

def fatorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

print(foo(4))
print(fatorial(4))
