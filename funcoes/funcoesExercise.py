# Crie uma função chamada quadrado(numero) que recebe um número como argumento e retorna o quadrado dele.Depois, use a função com um valor recebido via input() e exiba o resultado com print().

def quadrado(numero):
    numQuadrado = numero * numero
    return numQuadrado

resultado_quadrado = quadrado(int(input('Digite um numero inteiro: ')))
print(f'O resultado ao quadrado é: {resultado_quadrado}')

# ---------------------------------SOLUCAO DO PROFESSOR--------------------------------------

def quadrado(numero):
    return numero ** 2

numero_usuario = float(input('Digite um numero: '))
print(f'{numero_usuario} elevado ao quadrado é: {quadrado(numero_usuario)}')

# Crie uma função chamada apresentar_pessoa(nome, idade) que exibe a seguinte mensagem: "Nome: <nome> | Idade: <idade> anos" Chame a função passando valores diferentes.

def apresentar_pessoa(nome, idade):
    credenciais = print(f'Nome: {nome} | Idade: {idade} anos')
    return credenciais

apresentar_pessoa(input(f'Digite o seu nome: '), int(input(f'Digite a sua idade: ')))

# ---------------------------------SOLUCAO DO PROFESSOR--------------------------------------

def apresentar_pessoa(nome, idade):
    print(f'Nome: {nome} | Idade: {idade} anos')

apresentar_pessoa('Tony', 22)

# Crie uma função chamada verificar_par(numero) que retorna: "Par" se o número for par, "Ímpar" se for ímpar. Peça um número ao usuário com input(), chame a função e mostre o resultado.

def verificar_par(numero):
    if numero % 2 == 0:
        print('Par')
    else:
        print('Ímpar')

verificar_par(int(input('Digite um numero inteiro: ')))

# ---------------------------------SOLUCAO DO PROFESSOR--------------------------------------

def verificar_par(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

numero_user = int(input('Digite um numero inteiro: '))
print(f'O numero {numero_user} é {verificar_par(numero_user)}')
