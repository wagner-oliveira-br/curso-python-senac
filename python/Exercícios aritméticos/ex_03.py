''' Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais. '''

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
  print(f'o maior número é: {num1}')
  print(f'o menor número é: {num2}')

else:
  print(f'o maior número é: {num2}')
  print(f'o menor número é: {num1}')
if num1 == num2:
  print('Os números são iguais')