from functions import saudacao
from matematica import *
from meu_pacote.formatador import caixa_alta
from meu_pacote.numeros import eh_par
from perfil.usuario import criar_perfil
from perfil.validacao import idade_valida

nome = input('Digite o seu nome: ')
saudacao(caixa_alta(nome))

number1 = float(input('Agora digite um numero para saber qual seu valor dobrado e qual a sua metade: '))

dobro(number1)
metade(number1)
eh_par(number1)

# --------------------------------------------------------

usuarios = []

user = input('Digite o nome de usuario: ')
userAge = int(input('Digite sua idade: '))

if idade_valida(userAge) == True:
    usuarios.append(criar_perfil(user, userAge))
    print(f'O usuario {user} foi autorizado!')
else:
    print('Acesso negado! Menor de idade detectado.')

print(usuarios)

