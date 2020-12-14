arq = open('dados.txt', 'a')

for i in range(20):
  print(f'Máquina {i + 1}')
  ip = input('Endereço IP: ')
  hostname = input('Hostname: ')
  arq.write(f"{ip} - {hostname}\n")

arq.close()

arq = open('dados.txt', 'r')
for maquina in arq.read().splitlines():
  print(maquina)

arq.close()
