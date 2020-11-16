frase = input('Informe uma frase: ')

while (frase.find('  ') != -1):
    frase = frase.replace('  ', ' ')

frase = frase.strip()

print(frase.count(' ') + 1)
