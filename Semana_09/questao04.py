frase = input('Informe uma frase: ')
qtde = 0

for i in range(len(frase)):
    if (frase[i] == ' '):
        qtde += 1

print(qtde + 1)
