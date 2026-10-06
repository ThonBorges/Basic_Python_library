# Crie uma lista com 3 animais e mostre o primeiro e o último elemento.

animais = ['gorila', 'leão', 'girafa']

print(animais[0], animais[2])

# Dada a lista abaixo: livros = ["Python", "Java", "C++"]. Realize as seguintes ações: Adicione o livro "JavaScript", Remova o livro "Java", Troque "Python" por "Go", Mostre o tamanho da lista

livros = ["Python", "Java", "C++"]

livros.append("JavaScript")
livros.pop(1)
livros[0] = "Go"
print(len(livros))


# Dada a lista abaixo:

nomes = [ "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Giovana", "Hugo", "Isabela", "João", "Carla", "Lucas", "Mariana", "Nuno", "Olivia", "João", "Pedro", "Carla", "Rafael", "Ana" ]

#Mostre: Quantas vezes o nome Carla aparece / Qual o índice da primeira vez que ele aparece

print(nomes.count("Carla"))
print(nomes.index("Carla"))