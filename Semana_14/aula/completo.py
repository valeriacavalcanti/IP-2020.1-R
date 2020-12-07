arq = open('dados.txt', 'a')

for i in range(4):
    frase = input('Informe uma frase: ')
    arq.write(frase)
    arq.write('\n')

arq.close()

arq = open('dados.txt', 'r')

for linha in arq.read().splitlines():
    print(linha)

arq.close()
