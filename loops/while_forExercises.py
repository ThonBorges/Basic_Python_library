# Crie um programa que imprime os números de 10 até 1 usando um loop while.

contador = 1
while contador in range(1, 11):
    print(f'Contador atual: {contador}')
    contador += 1

# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

numeros = []
soma = 0

for i in range(5):
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)
    soma += numero

print(f'Numeros digitados: {numeros}')
print(f'O resultado total da soma dos 5 números é: {soma}')

# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).Quando o usuário digitar 0, o programa para e mostra o total economizado.

cofrinho = 0
depositos = []

while True: #While true diz para o sistema continuar indefinidamente, até que eu mande parar
    deposito = float(input("Digite o valor do depósito (0 - Para sair): R$ "))

    if deposito != 0:  #Colocada condicional if para tratar o 0 e não deixar ele entrar na adição da lista
        depositos.append(deposito)
        cofrinho += deposito
    else:
        print(f'Valores depositados: {depositos}\n Total depositado: R${cofrinho}' )
        break

# Crie um sistema de votação onde o usuário escolhe entre: 1. "Pizza", 2. "Hamburguer", 3."Sair". Enquanto ele não digitar "3", continue perguntando. No final, mostre quantos votos cada item recebeu

pizza = 0
hamburguer = 0

while True:
    votador = int(input(f"Vote no seu preferido: \n 1 - Pizza \n 2 - Hamburguer \n 3 - Sair \n"))

    if votador == 1:
        print(f'Ponto pra pizza!')
        pizza += 1
    elif votador == 2:
        print(f'Temos um hamburguer lover!')
        hamburguer += 1
    elif votador == 3:
        print(f'Obrigado pela participação, aqui estão os resultados: \n Pizza: {pizza} votos \n Hamburguer: {hamburguer} votos')
        break
    else:
        print(f'Número escolhido inválido!')

if pizza > hamburguer:
    print(f'Pizza é o grande ganhador com {pizza} votos!')
elif hamburguer > pizza:
    print(f'Hamburguer lovers ganharam em peso com {hamburguer} votos!')
else:
    print(f'Tivemos um empate, portanto suas paixões estão equilibradas!')