def multiplo(n1, n2):
    return n1 % n2 == 0

# PROGRAMA PRINCIPAL

num1 = int(input('Informe um valor: '))
num2 = int(input('Informe um valor: '))

print(num1, 'múltiplo', num2, multiplo(num1, num2))
