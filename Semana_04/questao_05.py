pessoas = 0
chocolates = 100

qtde = int(input("Quantidade: "))
while (qtde <= chocolates and pessoas < 99):
    chocolates -= qtde
    pessoas += 1
    qtde = int(input("Quantidade: "))

# 20(80) 30(50) 40(10) 50(X)
print(chocolates, pessoas)
