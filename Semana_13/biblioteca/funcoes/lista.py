def somar(lista):
    total = 0
    for e in lista:
        total += e
    return total

def maior(lista):
    m = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] > m):
            m = lista[i]

    return m
