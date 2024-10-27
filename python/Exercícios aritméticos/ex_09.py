'''
Faça um algoritmo para ler três números e se estes poderem formar um triângulo dizer se o triângulo é “Equilátero”, “Isóceles” OU “Escaleno”.
'''
def triangulo(x, y, z):
    return x + y > z and x + z > y and y + z > x

def tipo_triangulo(x, y, z):
    if x == y == z:
        return 'Equilátero'
    elif x == y or z == x or y == z:
        return 'Isósceles'
    else:
        return 'Escaleno'
    
def main():
    try:
        x = int(input('Digte o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        z = int(input('Digite o terceiro número: '))

        if triangulo(x, y, z):
            tipo = tipo_triangulo(x, y, z)
            print('O triângulo é {tipo}.')
        else:
            print('Esses números informados não podem formar o nosso triângulo.')
    except ValueError:
        print('Por favor, só insira números inteiros válidos para nosso triângulo')

if __name__ == "__main__":
    main()