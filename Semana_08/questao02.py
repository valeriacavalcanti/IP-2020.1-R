matriz1 = []
matriz2 = []
matriz3 = []

# criar as matrizes
for i in range(2):
    matriz1.append([0] * 3)
    matriz2.append([0] * 3)
    matriz3.append([0] * 3)

# Ler a matriz 1
print('Matriz 1:')
for i in range(2):
    for j in range(3):
        matriz1[i][j] = int(input())

# Ler a matriz 2
print('Matriz 2:')
for i in range(2):
    for j in range(3):
        matriz2[i][j] = int(input())

# Calcular a matriz 3
for i in range(2):
    for j in range(3):
        matriz3[i][j] = matriz1[i][j] + matriz2[i][j]

# Exibir a matriz 3
print('Matriz 3:')
print(matriz3)
