from util import adicionaProduto, buscaProduto, removeProduto, listaProduto

produtos = []

while True:

    print('''
    1 - Adicionar produto
    2 - Listar produtos
    3 - Buscar produto
    4 - Remover produto
    5 - Sair
    ''')
    opcoes = int(input('Digite a opcao desejada: '))

    match opcoes:
        case 1:
            adicionaProduto(produtos)
        case 2:
            print('----- ESTOQUE -----')
            listaProduto(produtos)
        case 3:
            buscaProduto(produtos)
        case 4:
            removeProduto(produtos)
        case 5:
            print(f'Encerrando sistema...')
            break
        case _:
            print('Escolha uma opcao valida!')
