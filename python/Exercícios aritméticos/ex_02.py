''' Faça um algoritmo para ler três números e imprimir a soma, média e produto dos números lidos. '''

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

soma = num1 + num2 + num3
media = soma / 3
produto = num1 * num2 * num3

print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')
print(f'O produto dos números é: {produto}')