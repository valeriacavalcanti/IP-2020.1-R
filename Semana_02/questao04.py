l1, l2, l3 = input().split()
l1, l2, l3 = int(l1), int(l2), int(l3)

if (l1 == l2) and (l1 == l3):
  print('equilatero')
elif (l1 != l2) and (l1 != l3) and (l2 != l3):
  print('escaleno')
else:
  print('isoceles')