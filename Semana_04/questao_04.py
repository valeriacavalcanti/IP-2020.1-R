num = int(input("Informe um número: "))
while (num > 0):
    # exibir os divisores
    for i in range(1, num + 1):
        if (num % i == 0):
            print(i, end = ' ')
    print()
    num = int(input("Informe um número: "))
