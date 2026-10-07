from util import adicionaProduto

print(f' Opcoes: \n'
      f' 1 - Adicionar produto\n'
      f' 2 - Listar produtos\n'
      f' 3 - Buscar produto\n'
      f' 4 - Remover produto\n'
      f' 5 - Sair\n'
      )

opcoes = input('Digite a opção desejada: ')

produtos = []

while True:
    match opcoes:
        case 1:
            produtos.append(adicionaProduto())
        case 2:
            print(produtos)
        case 3:
            ...
        case 4:
            ...
        case 5:
            print(f'Encerrando sistema...')
            break
        case _:
            print('Escolha uma opcao valida!')
