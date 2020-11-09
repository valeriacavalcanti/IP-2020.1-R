frase = input('Informe uma frase: ')

for i in range(len(frase)):
    if (frase[i] >= 'a') and (frase[i] <= 'z'):
        cod = ord(frase[i]) + 3
        # sempre que ultrapassar 122 (z), deve voltar para 'a' (97)
        if (cod > 122):
            cod = cod - 26 # 122 + 97 - 1
        print(chr(cod), end='')
    elif (frase[i] >= 'A') and (frase[i] <= 'Z'):
        cod = ord(frase[i]) + 3
        # sempre que ultrapassar 90 (Z), deve voltar para 'A' (65)
        if (cod > 90):
            cod = cod - 26 # 90 + 65 - 1
        print(chr(cod), end='')
    else:
        print(frase[i], end='')
