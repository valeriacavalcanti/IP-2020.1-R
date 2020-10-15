candidatos = []
votos = []
nulos = 0

for i in range(4):
    candidatos.append(int(input("Número: ")))
    votos.append(0)

for i in range(6):
    voto = int(input("Candidato: "))
    achei = False
    for j in range(4):
        if (voto == candidatos[j]):
            votos[j] += 1
            achei = True
            break

    if (achei == False): # if (not achei):
        nulos += 1

for i in range(4):
    print(f"Candidato ({candidatos[i]}): {votos[i]} votos")

print(nulos)
