def adicionaProduto(produtos):
    produto = input('Digite o nome do produto: ')
    quantidade = int(input('Quantidade: '))
    dados = {
        'produto': produto,
        'quantidade': quantidade
    }
    
    return produtos.append(dados) # O return nessa situacao esta adicionando os dados ao final da lista e devolvendo para produtos, que e um parametro que podera ser chamado na aplicacao principal.


def buscaProduto(produtos):
    produto = input('Digite o nome do produto: ')
    for nome in produtos:
        if nome['produto'] == produto:
            print(nome)
            return # O return dentro do if no loop, indica que quando a iteracao encontrar o valor buscado, ele pode encerrar completamente a funcao.
        
    else:
        print(f'Nenhum produto com o nome {produto} foi encontrado!')

def removeProduto(produtos):
    produto = input('Digite o nome do produto: ')
    for nome in produtos:
        if nome['produto'] == produto:
            produtos.remove(nome)
            print(f'O produto {nome['produto']} foi removido com sucesso!')
            return
    
    else:
        print(f'Nenhum produto com o nome {produto} foi encontrado!')


def listaProduto(produtos): # Nesse exemplo de lista, nao preciso usar return porque ja sendo printado o resultado
    for produto in produtos:
        print(f'\n Produto: {produto['produto']}\n Estoque: {produto['quantidade']}\n ')
