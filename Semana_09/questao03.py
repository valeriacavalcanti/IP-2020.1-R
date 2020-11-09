frase = input('Informe uma frase: ')
qtde_letra_mai = 0
qtde_letra_min = 0
qtde_numero = 0
qtde_especial = 0

for i in range(len(frase)):
    if ((frase[i] >= 'A') and (frase[i] <= 'Z')):
        qtde_letra_mai += 1
    elif ((frase[i] >= 'a') and (frase[i] <= 'z')):
        qtde_letra_min += 1
    elif ((frase[i] >= '0') and (frase[i] <= '9')):
        qtde_numero += 1
    else:
        qtde_especial += 1

print('Letras maiúsculas:', qtde_letra_mai)
print('Letras minúsculas:', qtde_letra_min)
print('Números:', qtde_numero)
print('Caracteres especiais:', qtde_especial)
