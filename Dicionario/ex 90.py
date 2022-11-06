#Dicionario

aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a media do {aluno["nome"]}: '))
if aluno['media'] >= 7.0:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é {v}')