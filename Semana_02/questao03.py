mes = input("Mês: ")

if (mes == 'jan') or (mes == 'mar') or (mes == 'mai') or (mes == 'jul') or (mes == 'ago') or (mes == 'out') or (mes == 'dez'):
  print(31)
elif (mes == 'fev'):
  print('28 ou 29')
else:
  print(30)