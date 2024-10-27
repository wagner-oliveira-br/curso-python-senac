cliente = []

print("         CADASTRO DO CLIENTE ⚇       ")

while True:
    nome = input('Digite seu nome completo: ')
    cpf = input('Digite seu CPF: ')
    numero = input('Digite seu número: ')

    cliente.append('nome: {nome} cpf: {cpf} e número: {numero}')

    resposta = input('quer adicionar mais algum cliente? (s/n): ').lower()
    if resposta != 's':
        break

print('---------------------------------')

print("         CLIENTES CADASTRADOS ✍       ")

for i, cliente in enumerate(cliente):

    print(f"\nCliente {i + 1}:")
    print(f"Nome: {cliente[0]}")
    print(f"CPF: {cliente[1]}")
    print(f"Número: {cliente[2]}")

print('---------------------------------')

