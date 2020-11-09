frase = input('Informe uma frase: ')
vogais = 'aeiou'
qtde = 0

for i in range(len(frase)):
    if (frase[i] in vogais):
        qtde += 1

print(qtde)
