def adicionaProduto():
    produto = input('Digite o nome do produto: ')
    quantidade = int(input('Quantidade: '))
    dados = {
        'produto': produto,
        'quantidade': quantidade
    }
    return dados