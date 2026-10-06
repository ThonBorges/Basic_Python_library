from util import gravaDespesa

contas = []
totalGastos = 0
maiorGasto = 0
maiorDespesa = ''

for i in range(5):
    contas.append(gravaDespesa())
    
print(f"\n----- RESUMO ------\n")

for conta in contas:
    totalGastos += conta['valor']

    if conta['valor'] > maiorGasto:
        maiorGasto = conta['valor']
        maiorDespesa = conta['despesa']

    print(f" {conta['despesa']} - R$ {conta['valor']:.2f}")
    
print(f'\n Maior despesa: {maiorDespesa} - R$ {maiorGasto:.2f}')
print(f"\n Total gasto: R$ {totalGastos:.2f}")
        



