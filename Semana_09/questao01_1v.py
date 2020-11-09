palavra = input('Informe uma palavra: ')
existe = False

for i in range(len(palavra)):
    if (palavra[i] == 'a'):
        existe = True
        break

if (existe == True):
    print('Existe')
else:
    print('Não Existe')
