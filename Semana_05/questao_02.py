notas = []
soma = 0

for i in range(10):
    notas.append(int(input("Informe a nota: ")))
    soma += notas[i]

media = soma / 10

for i in range(10):
    if (notas[i] > media):
        print(notas[i])
