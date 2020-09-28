n1, n2 = input("Informe dois valores: ").split()
n1, n2 = int(n1), int(n2)

for i in range(n1, n2 + 1):
    if (i % n1 == 0):
        print(i)
