from util import consultaSaldo, depositoBancario, saqueBancario
import time

print('''
    Bem vindo ao Banco BOAVIDA!
    Para iniciar seu cadastro, por gentileza preencha as informacoes abaixo!
''')

while True:

    userCPF = input('Digite seu CPF sem pontuacoes/mascara: ')
    userPasswd = input('Nova senha: ')

    if userCPF.isdigit() and len(userCPF) == 11:
        print('Cadastro Realizado com sucesso!')
        time.sleep(1.5)
        break
    else:
        print('CPF Invalido, tente novamente apenas com numeros!')

contaBancaria = {
    'cpf': userCPF,
    'senha': userPasswd,
    'saldo': 0,
    'tentativasVigentes': 3
}

nome = input('Digite seu nome ou apelido: ')

while True:
    user = input('Login (CPF sem pontuacoes): ')
    passwd = input('Senha: ')

    if user == contaBancaria['cpf'] and passwd == contaBancaria['senha']:
        print(f'\nBem vindo ao Banco BOAVIDA, {nome}! O que deseja fazer hoje?\n')
        break
    elif user != contaBancaria['cpf']:
        print('CPF nao encontrado, tente novamente!')
    elif passwd != contaBancaria['senha']:
        contaBancaria['tentativasVigentes'] -= 1
        print(f'Senha incorreta, voce possui {contaBancaria["tentativasVigentes"]} tentativas vigentes...')
        if contaBancaria['tentativasVigentes'] == 0:
            print('Voce atingiu o limite de 03 tentativas, por seguranca tente novamente apos 5 segundos.')
            time.sleep(5)

time.sleep(2)

while True:

    print('''
        === BANCO BOAVIDA ===

        1 - Consultar saldo
        2 - Depositar
        3 - Sacar
        4 - Sair

    ''')

    try:
        opcao = int(input('Opcao escolhida: '))

        if opcao != int:
            match opcao:
                case 1:
                    consultaSaldo(contaBancaria['saldo'])
                    time.sleep(3)
                case 2:
                    contaBancaria['saldo'] = depositoBancario(contaBancaria['saldo'], nome)
                case 3:
                    contaBancaria['saldo'] = saqueBancario(contaBancaria['saldo'], nome)
                case 4:
                    print(f'\nObrigado por escolher o Banco BOAVIDA {nome}!\n\nEncerrando sistema... \n')
                    time.sleep(3)
                    break
                case _:
                    print('Selecione uma opcao valida para o sistema!')
                    time.sleep(3)

    except ValueError:    
        print('A opcao escolhida precisa ser um numero!')
        time.sleep(3)