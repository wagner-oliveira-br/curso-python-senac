''' Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B. '''

A = int(input('Digite o número A: '))
B = int(input('Digite o número B: '))

if A % B == 0:
  print(f'Número {A} é divisível por {B}')
else :
  print(f'Número {A} não é divisível por {B}')