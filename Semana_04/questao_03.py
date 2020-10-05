num = int(input("Informe um número: "))

# número mágico: múltiplo de 3 E par
while((num % 3 != 0) or (num % 2 != 0)):
    num = int(input("Informe um número: "))

print(num)
