lista = []

# 1 2 3 4 5 1 2 3 8 9

num = int(input())
while (num != 0):
    existe = False
    for i in range(len(lista)):
        if (num == lista[i]):
            existe = True
            break
    if (existe == False):
        lista.append(num)
    # print('Lista temporária: ', lista)
    num = int(input())

print(lista)
