import sys

def realizar_saque(saldo):
    try: 
        saque = float(input('Digite o valor do seu saque: '))
        if saque <= 0:
            print('O valor do saque deve ser positivo!')
        elif saque <= saldo:
            saldo -= saque
            print('O seu saque realizado com sucesso!')
        else: 
            print('O seu saldo é insuficiente!')
    except ValueError:
        print('Essa entrada é inválida, Po favor, digite um número.')
    
    return saldo

def main():
    saldo_inicial = 1000
    saldo = saldo_inicial

    print('Bem-vindo ao nosso sitema de saque.')

    while True:
        print(f'Saldo atual: {saldo:.2f}')
        continuar = input('Você deseja realizar um saque? (s/n)').lower()

        if continuar == 's':
            saldo = realizar_saque(saldo)
        elif continuar == 'n':
            print('Saindo do sitema de saque. Se precisar fazer mais saques, inicialize o sitema novamente. Até logo!')
            sys.exit('Encherrando o programa')

if __name__ == '__main__':
    main()
