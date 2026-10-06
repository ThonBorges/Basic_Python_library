opcao = int(input('Escolha uma opção de 1 a 3: '))

match opcao:
    case 1:
        print('opção 1 escolhida!')
    case 2:
        print('opção 2 escolhida!')
    case 3:
        print('opção 3 escolhida!')
    case _:
        print('opção inv�lida!')