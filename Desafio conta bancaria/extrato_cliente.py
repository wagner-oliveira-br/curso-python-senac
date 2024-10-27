saldo = 9000.0  

print(f'O seu atual saldo é: R$ {saldo:.2f}')

while True:
    entrada = input('Digite o valor do seu saque (ou "sair" para simplesmente sair): ')
    
    if entrada.lower() == "sair":
        print('Encerrando o sistema. Até já!')
        break
    
    try:
        valor_saque = float(entrada)

        if valor_saque <= 0:
            print('O valor do saque tem que ser maior que zero. Tente novamente.')
        elif valor_saque > saldo:
            print(f'Saldo insuficiente. Seu saldo atual é: R$ {saldo:.2f}')
        else:
            saldo -= valor_saque
            print(f'Saque realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}')

    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'sair'.")

print('Obrigado por usar o nosso sistema! Até a próxima')