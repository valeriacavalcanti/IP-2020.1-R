times = []
votos = []

for i in range(4):
    times.append(input("Time: "))
    votos.append(0)

for i in range(6):
    voto = input('Voto: ')
    for j in range(4):
        if (voto == times[j]):
            votos[j] += 1
            break

print(times)
print(votos)

# Times: flamengo(2) - palmeiras(2) - sport(1) - botafogo(1)
# votos: flamengo - flamengo - palmeiras - sport - botafogo - palmeiras
