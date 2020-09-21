mes, dia = input().split()
dia = int(dia)

if (mes == 'jan') or (mes == 'fev'):
  print('verão')
elif (mes == 'mar'):
  if (dia < 20):
    print('verão')
  else:
    print('outono')
elif (mes == 'abr') or (mes == 'mai'):
  print('outono')
elif (mes == 'jun'):
  if (dia < 21):
    print('outono')
  else:
    print('inverno')
elif (mes == 'jul') or (mes == 'ago'):
  print('inverno')
elif (mes == 'set'):
  if (dia < 22):
    print('inverno')
  else:
    print('primavera')
elif (mes == 'out') or (mes == 'nov'):
  print('primavera')
else:
  if (dia < 21):
    print('primavera')
  else:
    print('verão')