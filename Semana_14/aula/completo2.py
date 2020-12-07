import os

arq = open('dados.txt', 'w+')

for i in range(4):
    frase = input('Informe uma frase: ')
    arq.write(frase)
    arq.write('\n')

# posiciona o cursor no início (SEEK_SET)
arq.seek(os.SEEK_SET)

for linha in arq.read().splitlines():
    print(linha)

arq.close()
