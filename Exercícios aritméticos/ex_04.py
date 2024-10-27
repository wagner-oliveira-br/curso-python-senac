''' Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou impar. '''  

A = int(input('Digite o número A:'))
B = int(input('Digite o número B:'))

if A % 2 == 0:
  print(f'O número {A} é par')
else:
  print(f'O número {A} é impar')