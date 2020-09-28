qt_adol = 0
qt_adul = 0
qt_ido = 0

for i in range(1, 5):
    idade = int(input(f"Pessoa {i}: "))
    if (idade <= 17):
        qt_adol += 1
    elif (idade <= 70):
        qt_adul += 1
    else:
        qt_ido += 1

print(qt_adol, qt_adul, qt_ido)
