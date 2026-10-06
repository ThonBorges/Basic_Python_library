# Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".

notaAlcancada = float(input('Digite a sua nota da prova: '))

mediaParaPassar = 6

if notaAlcancada >= mediaParaPassar :
    print(f'Você foi aprovado!')
else: 
    print('Reprovado!')

# Verificação de Diferença: Crie um código que peça para o usuário inserir dois nomes. Depois verifique se os dois nomes são diferentes. Se forem, exiba "Os nomes digitados são diferentes.".

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')

if nome1 == nome2:
    print('Os nomes digitados são iguais')
else:
    print('Os nomes digitados são diferentes')

# Elegibilidade para um Evento (Idade Mínima): Imagine um evento para maiores de 15 anos. Crie um código que pergunte a idade do usuário. Verifique se a idade do usuário é maior ou igual a 15. Se for, exiba "Você pode participar do evento!".

idade = int(input('Digite sua idade para continuar: '))

if idade <= 15 : 
    print(f'Sua idade ({idade} anos) é inferior à idade mínima permitida!')
elif idade >= 15 and idade <= 50 :
    print(f'Hmmmm... Ta na idade da maldade né danado.')
else : 
    print(f'Com {idade} anos, cê já ta véi demais pra isso.')

# Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim: Nota 9 ou 10: "Excelente!", Nota 7 ou 8: "Muito bom", Nota 5 ou 6: "Regular", Menor que 5: "Ruim"

notaFilme = int(input('Após assistir ao filme, de 0 a 10, o quanto você classificaria esse filme: '))

if notaFilme < 5:
    print('Ruim')
elif notaFilme >= 5 and notaFilme <= 6:
    print('Regular')
elif notaFilme >= 7 and notaFilme <= 8:
    print('Muito Bom')
else:
    print('Excelente')

# Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são: O valor da compra deve ser maior ou igual a 100, E o cliente precisa estar cadastrado no programa de fidelidade. Se as duas condições forem verdadeiras, mostre: "Frete grátis aplicado!", Caso contrário: "Frete não disponível gratuitamente."

valorCompra = float(140)
usuarioLogado = True

if valorCompra >= 100 and usuarioLogado == True:
    print('Frete grátis Aplicado!')
else:
    print('Frete não disponível gratuitamente.')