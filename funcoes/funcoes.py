def saudacao():
    print('Olá mundo!')
saudacao()

# -----------------------------------------------------------------

def saudacao(nome):
    print(f'Olá {nome}')
saudacao('dressinha')

# -----------------------------------------------------------------

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f'A soma do {numero1} e {numero2} é {resultado}')

somar(24, 36)
somar(11, 56)
somar(2, 6)

# -----------------------------------------------------------------

def somar(num1, num2):
    resultado = num1 * num2
    return resultado

resultado1 = somar(2, 10)
print(f'{resultado1}')

# -----------------------------------------------------------------

def calculo_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final

resultado_compra = calculo_desconto(290, 5)
print(f'O valor da compra é de R$ {resultado_compra}')