import time

def consultaSaldo(saldo):
    print(f'Saldo atual disponivel: R$ {saldo:.2f}')

# ----------------------------------------------------------------------

def depositoBancario(saldo, nome):
    while True:
        try:
            valor = float(input('Valor a ser depositado: R$ '))

            if valor <= 0:
                print('Digite um valor maior que zero!')
                continue

            saldo += valor

            print('Processando seu deposito...')
            time.sleep(2)
            print(f'Deposito realizado com sucesso, {nome}! Voce possui agora R$ {saldo}.')
            time.sleep(2)
            break

        except ValueError:
            print('Valor invalido! Digite apenas numeros.')

    return saldo

# ----------------------------------------------------------------------

def saqueBancario(saldo, nome):
    while True:
        try:
            valor = float(input('Valor a ser sacado: R$ '))
    
            if valor <= 0:
                print('O valor do saque deve ser maior que zero!')
                continue

            if valor > saldo:
                print(f'Saldo insuficiente! Disponivel: R$ {saldo:.2f}')
                continue
    
            saldo -= valor

            print('Saque sendo processado...')
            time.sleep(2)    
            print(f'Saque realizado com sucesso, {nome}! Voce possui agora R$ {saldo}.')
            time.sleep(2)
            break
    
        except ValueError:
            print('Valor invalido! Digite apenas numeros.')
    
    return saldo