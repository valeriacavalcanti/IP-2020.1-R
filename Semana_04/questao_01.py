pos = 0
neg = 0

num = int(input("Informe um número: "))
while (num != 0):
    if (num > 0):
        pos += 1
    else:
        neg += 1
    num = int(input("Informe um número: "))

print(pos, neg)
