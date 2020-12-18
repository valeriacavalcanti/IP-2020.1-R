def somar(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

def somar_recursiva(num):
    if (num == 0):
        return 0
    return num + somar_recursiva(num - 1)

# PP
print(somar(10))
print(somar_recursiva(10))
