def divisor(n1, n2):
    return n1 % n2 == 0

# PROGRAMA PRINCIPAL

num1 = int(input('Informe um valor: '))
num2 = int(input('Informe um valor: '))

print(num2, 'divisor', num1, divisor(num1, num2))
