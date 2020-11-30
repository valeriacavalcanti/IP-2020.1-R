def divisores(num):
    lista = []
    for i in range(1, num+1):
        if (num % i == 0):
            lista.append(i)

    return lista

def primo(num):
    return len(divisores(num)) <= 2

def perfeito(num):
    d = divisores(num)
    soma = 0
    for i in range(len(d) - 1):
        soma += d[i]

    return soma == num
