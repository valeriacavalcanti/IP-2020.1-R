notas = []

# Declarar a matriz
for i in range(10):
    notas.append([0] * 4)

# Ler as notas
for i in range(10):
    for j in range(4):
        notas[i][j] = int(input())

# procurar o maior valor
# Indica que na primeira posição (0 0) tem o maior valor
m_i = m_j = 0
# Comparar com todas as demais posições da matriz
for i in range(10):
    for j in range(4):
        if (notas[i][j] > notas[m_i][m_j]):
            m_i = i
            m_j = j

# Exibir o resultado
print('Maior =', notas[m_i][m_j], '- Posiçao:', m_i, m_j)
print(notas)
