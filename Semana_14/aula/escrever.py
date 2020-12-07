arq = open('dados.txt', 'w')
#lista = []

for i in range(4):
    frase = input('Informe a frase: ')
    #lista.append(frase)
    arq.write(frase)
    arq.write('\n')

#arq.writelines(lista)

arq.close()
