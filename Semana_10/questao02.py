qtl = qtn = qte = 0

frase = input("Inforeme uma frase: ")

for i in range(len(frase)):
    if (frase[i].isalpha()):
        qtl += 1
    elif (frase[i].isdigit()):
        qtn += 1
    else:
        qte += 1

print(qtl)
print(qtn)
print(qte)
