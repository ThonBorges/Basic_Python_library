def gravaDespesa():
    despesa = input('Digite o nome da despesa a ser gravada: ')
    valorDespesa = float(input('Valor da despesa: R$ '))
    dados = {
        'despesa': despesa,
        'valor': valorDespesa
    }

    return dados