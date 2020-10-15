numero = int(input("Informe um valor: "))
binario = []

num = numero

while (num // 2 != 0):
    binario.append(num % 2)
    num = num // 2

binario.append(num)

binario.reverse()

print(bin(numero)[2:])
print(binario)
