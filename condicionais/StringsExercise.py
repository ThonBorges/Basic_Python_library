# Peça ao usuário para digitar uma palavra. Mostre: A primeira letra e a ultima letra.

varRecebe = input("Digite uma palavra: ")

print(f'A primeira letra é {varRecebe[0]}, e a última é {varRecebe[-1]}')

# Peça ao usuário uma frase e dois números: início e fim. Mostre o fatiamento da frase entre esses índices.

varRecebe2 = input('Digite uma frase: ')
numRecebe = int(input('Agora o primeiro numero inteiro dentre o total de palvras da sua frase: '))
numRecebe2 = int(input('Agora o segundo numero inteiro dentre o total de palvras da sua frase: '))

print(f'O trecho da frase é: {varRecebe2[numRecebe:numRecebe2]}')

# Peça ao usuário para escrever uma mensagem. Verifique se ela contém a palavra "bomba", e imprima um alerta se sim.

varRecebe3 = input('Digite uma frase sobre um objeto que exploda: ')

if "bomba" in varRecebe3:
    print('Sim')
else:
    print('Não')

# Dada uma variável frase = "    @prendendo @ progr@m@r   "  com espaços nas pontas e letras bagunçadas, o programa deve: Remover espaços do início/fim, Trocar todas as letras "@" por "a", Colocar a primeira letra de cada palavra em maiúsculo

frase = "    @prendendo @ progr@m@r   "

print(frase.replace("@", "a").strip().title())