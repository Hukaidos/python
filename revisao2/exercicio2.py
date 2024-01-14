alunos = []
for i in range(2):
    nome = str(input(f'Nome do {i+1}º aluno: '))
    idade = int(input('Idade do aluno: '))
    turma = str(input('Turma: '))
    cpf = str(input('Cpf:'))
    
    print('\n','-='*30,'\n')

    aluno = {
        'nome':nome,
        'idade':idade,
        'turma':turma,
        'cpf':cpf
    }

    alunos.append(aluno)


for x,y in enumerate(alunos):
    print(f"""
    {x+1}º Aluno
    Nome: {y['nome']}
    idade: {y['idade']}       
    turma: {y['turma']}       
    cpf: {y['cpf']}       
""")

