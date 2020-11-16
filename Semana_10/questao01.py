qtde = 0
vogais = 'aeiou'

frase = input("Inforeme uma frase: ")

for i in range(len(frase)):
    if (frase[i] in vogais):
        qtde += 1

print(qtde)
