pessoas = 0
chocolates = 4

qtde = int(input("Quantidade: "))
while (qtde <= chocolates and pessoas < 3):
    chocolates -= qtde
    pessoas += 1
    qtde = int(input("Quantidade: "))

# 20(80) 30(50) 40(10) 50(X)
print(chocolates, pessoas)
