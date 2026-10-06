# Dicionarios funcionam em como JSONs
# pessoa["idade"] = 28 >> Retornou o valor presente na propriedade idade
# print(pessoa["idade"]) >> retorou no console o valor da propriedade idade
# del pessoa ["cidade"] >> Irá deletar o atributo/propriedade cidade
# print(pessoa["profissoes"][0]) >> Irá retornar os dados do primeiro objeto encontrado que são as informações do ID 1106
# print(pessoa.keys()) >> retorna todas as chaves da nossa estrutura
# print(pessoa.values()) >> faz a mesma coisa porem agora para os valores
# print(pessoa.items()) >> traz tanto a chave quanto os valores
# print(pessoa.get("telefone")) >> tentará buscar uma informação assim como os demais, porém se a info não existir, não retornará erros e não quebra o sistema. O GET é uma boa pratica para busca de dados
# print(pessoa.pop("idade")) >> remove a propriedade idade
# Dicionarios sempre serão usados quando tem ligar um nome a um valor


pessoa = {
    "nome": "Borgz",
    "idade": 28,
    "cidade": "Floripa",
    "profissoes": [
        {
            "id": 1106,
            "departamento": "Implantações",
            "setor": "tecnologia"
        },
        {
            "id": 1115,
            "departamento": "Desenvolvimento",
            "setor": "tecnologia"
    }
    ]
}

print(pessoa["profissoes"][0])
print(pessoa.keys())
print(pessoa.values())

valores = list(pessoa.values())
print(valores[2]) 
# Naturalmente, quando voce usa keys ou values e tenta passar parametro para acessar somente um indice, o python gera erro, porque essas funções são baseadas em um loop. Para fazer essa ação, usando o método acima, você encapsula o dicionario em uma lista e através disso você pode acessar o valor como um indice e filtrar somente aquilo que te é necessario no momento
