nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')
numero = input('Digite o número: ')
sexo = input('Digite o sexo: ')

cliente = [nome, cpf, numero, sexo]
clientes = [cliente]

print('Cadastrado do nome: {nome} número: {numero} cpf: {cpf} e sexo {sexo}')

print('-----------------')

print("Clientes cadastrados: ")
print(f"Nome: {clientes[0][0]}")
print(f"CPF: {clientes[0][1]}")
print(f"Número: {clientes[0][2]}")
print(f"Sexo: {clientes[0][3]}")

print('-----------------')