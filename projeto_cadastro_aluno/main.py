# ------------------------------- FUNÃÃES -----------------------------------------------

def adicionarAluno():
    nome = input('Aluno: ')
    idade = int(input('Idade: '))
    while True:
        nota = float(input('Nota: '))
        if nota >= 0 and nota <= 10:
          break
    
        else:
            print(f'digite um nÃºmero de nota vÃ¡lido entre 0 e 10.')
    dados = {
        'nome': nome,
        'idade': idade,
        'nota': nota 
    }
    listaAlunos.append(dados)
    print(f'Aluno {nome} adicionado com sucesso!')

def listar_alunos():
    for aluno in listaAlunos:
        print(f'\n Nome: {aluno['nome']},\n Idade: {aluno['idade']},\n Nota: {aluno['nota']},\n {'='*30}\n')

def buscarAluno(nome_do_aluno):
    if len(listaAlunos) == 0:
        print(f'Nenhum aluno encontrado!')
    
    for aluno in listaAlunos:
        if aluno ['nome'].lower() == nome_do_aluno:
            print(f'\n Nome: {aluno['nome']},\n Idade: {aluno['idade']},\n Nota: {aluno['nota']},\n')
            break
        else:
            print(f'Esse aluno nÃ£o foi encontrado')

def removerAluno(aluno_removido):
    if len(listaAlunos) == 0:
        print(f'A lista de alunos estÃ¡ vazia')

    for aluno in listaAlunos:
        if aluno ['nome'].lower() == aluno_removido:
            listaAlunos.remove(aluno)
            print(f'O aluno {aluno_removido} foi removido da lista.')
            break
        else:
            print('Aluno nÃ£o encontrado!')

def mediaNotas():
    if len(listaAlunos) == 0:
        print(f'A lista de alunos estÃ¡ vazia')

    soma = 0
    for alunos in listaAlunos:
        soma += alunos['nota']

    media = soma / len(listaAlunos)
    print(f'A mÃ©dia das notas dos alunos Ã© {media:.2f}')


# -------------------------------- PROGRAMA ----------------------------------------------

listaAlunos = []

while True:

    opcoes = int(input(
    "Menu de OpÃ§Ãµes:\n"
    "1 - Adicionar aluno\n"
    "2 - Listar todos os alunos\n"
    "3 - Buscar aluno pelo nome\n"
    "4 - Remover aluno\n"
    "5 - Mostrar mÃ©dia geral das notas\n"
    "6 - Sair\n"
    "OpÃ§Ã£o selecionada = "
    ))

    match opcoes:
        case 1:
            adicionarAluno()

        case 2:
            listar_alunos()
    
        case 3:
            nome_aluno = input('Digite o nome do aluno que deseja buscar: ')
            buscarAluno(nome_aluno)

        case 4:
            alunoRem = input('Digite o nome do aluno que deseja remover: ')
            removerAluno(alunoRem)

        case 5:
            mediaNotas() 
        
        case 6:
            print(f'Finalizando operaÃ§Ãµes...')
            break

        case _:
            print(f'OpÃ§Ã£o invÃ¡lida!')


    












