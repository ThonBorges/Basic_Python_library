# Crie um codigo onde e solicitado para o usuario inserir dois valores: o ano atual, e o ano de nascimento. O sistema deve calcular quantos anos ele tem de acordo com essas informacoes e exibir no console.

ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
sua_idade = ano_atual - ano_nascimento
print(f'Subtraindo o ano de {ano_atual} com o ano {ano_nascimento} de seu nascimento, sua idade e {sua_idade}');


# Crie um codigo onde o usuario deve inserir dois numeros e exiba a soma, subtracao, multiplicacao e divisao deles.

primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero =  int(input('Digite o segundo numero: '))

soma_numeros = primeiro_numero + segundo_numero
subtracao_numeros = primeiro_numero - segundo_numero
mult_numeros = primeiro_numero * segundo_numero
divis_numeros = primeiro_numero / segundo_numero

print(soma_numeros, subtracao_numeros, mult_numeros, divis_numeros)

# ----------------------------------------------------------------------------------------------------------------------
