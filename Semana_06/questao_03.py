cpf = list(input())

# calculando o primeiro dígito verificador
soma = 0
for i in range(len(cpf)):
    cpf[i] = int(cpf[i])
    soma += (cpf[i] * (10 - i))

resto = soma % 11

if (resto < 2):
    cpf.append(0)
else:
    cpf.append(11-resto)

# calculando o segundo dígito verificador
soma = 0

for i in range(len(cpf)):
    soma += cpf[i] * (11 - i)

resto = soma % 11

if (resto < 2):
    cpf.append(0)
else:
    cpf.append(11 - resto)

print(cpf)
