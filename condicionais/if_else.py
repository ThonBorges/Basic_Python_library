# Exemplo de condicional if em python, observe que o python é chato com identação, se a linha tiver em posição diferente, vai quebrar

idade = int(input('Digite sua idade para continuar: '))

if idade <= 17 : 
    print(f'Sua idade ({idade} anos) é inferior à idade mínima permitida!')
elif idade >= 18 and idade <= 50 :
    print(f'Hmmmm... Ta na idade da maldade né danado.')
else : 
    print(f'Com {idade} anos, cê já ta véi demais pra isso.')


# ---------------------------------------

user = 'ocarinha ali'
passwd = 'loudbetterthannrg'

userInput = input('Usuário: ')
passwdInput = input('Senha: ')

if userInput == user and passwdInput == passwd : 
    print(f'Acesso liberado!')
elif userInput != user :
    print(f'Usuário Incorreto!')
else :
    print(f'Senha Incorreta!')
