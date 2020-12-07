'''
    ler 10 valores:
        - soma desses valores - ok
        - média desses valores - ok
        - quantidade de números com valor acima da média - ok
        - quantidade de números com valor abaixo da média - vocês
        - maior valor - ok
        - menor valor - vocês
'''

def somar(lista):
    total = 0
    global qtde
    for i in range(len(lista)):
        qtde += 1
        total += lista[i]
    return total

def media(lista):
    return somar(lista)/len(lista)

# 1.0v
def acima_media_1v(lista):
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] > media(lista)):
            qtde += 1

    return qtde

# 2.0v
def acima_media_2v(lista):
    m = media(lista)
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] > m):
            qtde += 1
    return qtde


# PROGRAMA PRINCIPAL

qtde = 0
numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(100000):
    acima_media_1v(numeros)
print('terminou')
