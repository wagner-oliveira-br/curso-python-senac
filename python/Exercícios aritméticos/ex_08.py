'''
Faça um algoritmo para ler três números e imprimir se estes podem ou não formar um triângulo.
'''
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

if x + y > z and x + z > y and z + y > x:
    print('Esses números podem formar um triângulo :)')
else:
    print('Esses números não podem formar um triângulo :/')