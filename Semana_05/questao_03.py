nomes = []
valores = []
soma = 0

for i in range(4):
    nomes.append(input("Empresa: "))
    valores.append(float(input("Valor: ")))
    soma += valores[i]

media = soma / 4

for i in range(4):
    if (valores[i] < media):
        print(nomes[i])
