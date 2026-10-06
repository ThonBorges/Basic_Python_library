# contador = 1

# while contador <= 5:
#     print(f'Contando: {contador}')
#     contador += 1

# ---------------------------------------------------------

# senha = ''
# while senha != 'sss':
#     senha = input(f"Digite sua senha: ")
# print ("senha correta!")

# ----------------------------------------------------------

# for numero in range(1, 6):
#     print(numero)

# -----------------------------------------------------------

# frutas = ['banana', 'uva', 'laranja']

# for fruta in frutas:
#     print(f'A fruta atual: {fruta}')

# -----------------------------------------------------------

# for multiplicador in range(1, 11):
#     for multiplicado in range(1, 11):
#         print(f'{multiplicado} x {multiplicador} = {multiplicado * multiplicador}')

# ------------------------------------------------------------

# pessoas = ['ana', 'bruno', 'fernanda', 'daniel', 'felipe']
# for nome in pessoas:
#     print(f"Verificando: {nome}")
#     if nome == 'daniel':
#         print(f"Nome encontrado: {nome}")
#         break
# print ("Busca encerrada")

# ------------------------------------------------------------

for numero in range(1, 11):
    if numero %2 == 0:
        continue
    print(f'Numero: {numero}')