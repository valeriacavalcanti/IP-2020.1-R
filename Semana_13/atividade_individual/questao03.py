# misterio verifica se um elemento está contido na lista.

def misterio_recursiva(lista, n):
    if (len(lista)) == 0:
        return False
    elif (lista[0] == n):
        return True
    else:
        return misterio_recursiva(lista[1:], n)

def misterio_1v(lista, n):
    for elemento in lista:
        if (elemento == n):
            return True

    return False

def misterio_2v(lista, n):
    return n in lista

## PP

lista = [10, 20, 30, 40]

print(misterio_recursiva(lista, 20))
print(misterio_1v(lista, 20))
print(misterio_2v(lista, 20))

print(misterio_recursiva(lista, 60))
print(misterio_1v(lista, 60))
print(misterio_2v(lista, 60))
