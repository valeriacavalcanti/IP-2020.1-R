
try:
    arq = open('dados.txt', 'r')
    '''
        obter todos os caracteres que estão no arquivo
        dados = arq.read()
        for letra in dados:
            print(letra)
    '''
    # obter todos os caracteres que estão no arquivo
    # separados por linha
    dados = arq.read().splitlines()
    #dados = arq.readlines()
    for linha in dados:
        print(linha)

    arq.close()
except FileNotFoundError:
    print('Algum problema aconteceu')


