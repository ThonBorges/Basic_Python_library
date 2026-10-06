frutas = ['maçã', 'laranja', 'goiaba']
frutas.append('melancia') #Adiciona melancia ao final da lista
# frutas.remove('banana') #Remove banana da lista
# frutas[2] = 'uva' #Substitui a fruta do indice 2 por uva
# print(len(frutas)) #Retorna a quantidade de indices presentes numa lista
# frutas.insert(1, 'uva') #Faz a mesma função de adição do append, porém indicando em qual posição
# frutas.pop(1) #Remove o item indicado no indice. Se não for passado nenhum indice, a função removerá o ultimo item da lista.
# frutas.sort() #Organiza em ordem alfabetica os itens
# frutas.clear() # limpa a lista toda
# print(frutas.index('banana')) #Localiza qual o indice do item buscado
# print(frutas.count('maçã')) #Retorna quantas vezes o registro maçã foi encontrado na lista

frutas2 = frutas.copy() #vai criar uma cópia da lista original e armazenar na memoria

frutas2.append('Mamão')
frutas2.append('Limão')

print(frutas2)
print(frutas)

# tuplas são listas imutáveis, ou seja, funções que adicionam, removem, inserem ou fazem qualquer tipo de modificação não é possivel, porém funções que não alteram como saber o indice de tal informação pode ser usado normalmente. Enquanto usamos [] para listas, tuplas são declaradas com parenteses

# Exemplo de tupla: carros = ('Nissan', 'Honda', 'Chevrolet')