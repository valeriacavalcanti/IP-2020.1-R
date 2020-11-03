matriz = []

# Declarar a matriz
for i in range(5):
    matriz.append([0] * 5)

# Ler a matriz
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input())

# Verificando se é uma matriz identidade
identidade = True
for i in range(5):
    for j in range(5):
        if (i == j) and (matriz[i][j] != 1):
            identidade = False
            break
        elif (i != j) and (matriz[i][j] != 0):
            identidade = False
            break
    if (identidade == False):
        break

print(matriz)
print(identidade)
