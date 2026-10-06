# Crie um dicionário chamado livro com as chaves: "titulo", "autor" e "ano". Depois, mostre cada valor usando print().

livro = {
    "titulo": "The books on the table",
    "autor": "fulano",
    "ano": 2019
}

print(livro.values())

# Peça para o usuário digitar nome e idade. Guarde esses dados em um dicionário chamado usuario.Depois, verifique se a idade é maior ou igual a 18: Se sim, imprima: "Acesso liberado para {nome}", Se não, imprima: "Acesso negado para {nome}"

username = input("Digite o seu nome: ")
userAge = int(input('Digite sua idade: '))

account = {
    "name": username,
    "age": userAge
}

if userAge >= 18:
    print(f'Acesso liberado para {username}')
else:
    print(f'Acesso negado para {username}')


# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário. Se o usuário e a senha estão corretos → "Login bem-sucedido", Senão → "Usuário ou senha incorretos"

loginUser = input('Login: ')
passwdUser = input('Senha: ')

correctAccount = {
    "login": "ThonBorges",
    "passwd": "7070senaoder70denovo"
}

userAccount = {
    "login": loginUser,
    "passwd": passwdUser
}

if userAccount["login"] == correctAccount["login"] and userAccount["passwd"] == correctAccount["passwd"]:
    print(f'Login bem-sucedido!')
else:
    print(f'Acesso negado!')