# Crie um sistema simples de opções bancárias para o usuário navegar no terminal ATM. As opções devem listar o saldo da conta, o valor de saque maximo no dia e a tarifa por cada saque.

saldoConta = 'R$ 10.000,00'
saqueMaximoPermitido = 'R$ 2.000,00'
tarifaPorSaque = 'R$ 5,25'

opcoes = int(input('Digite uma das Opções a seguir: \n'
            '1 - Ver saldo da conta\n'
            '2 - Ver valor máximo de saque permitido\n'
            '3 - Ver tarifa por saque\n'
            '4 - Sair\n'
            'Opção escolhida >> '
            ))

match opcoes:
    case 1:
        print(f'O saldo atual da conta é de {saldoConta}')
    case 2:
        print(f'O saque máximo permitido por dia é de {saqueMaximoPermitido}')
    case 3:
        print(f'A tarifa cobrada por saque é de {tarifaPorSaque}')
    case 4:
        print('Operação finalizada!')
    case _:
        print('Opção inválida.')


