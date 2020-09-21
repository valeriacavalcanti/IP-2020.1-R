letra = input('Letra: ')

if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
  print('vogal')
elif (letra == 'y'):
  print('vogal / consoante')
else:
  print('consoante')