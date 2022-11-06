pessoas = dict()
cadastro = list()
soma = media = 0
while True:
    pessoas['nome'] = str(input('Digite o nome: '))
    while True:
        pessoas['sexo'] = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro, tente novamente!')
    pessoas['idade'] = int(input('Digite a idade: '))
    soma += pessoas['idade']
    cadastro.append(pessoas.copy())
    pessoas.clear()
    while True:
        resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro, tente novamente!')
    if resp in 'Nn':
        break
media = soma / len(cadastro)
print(f'O numero de pessoas cadastradas é {len(cadastro)}')
print(f'A media de idade das pessoas é: {media}')
print('As mulheres cadastradas foram: ', end='')
for c in cadastro:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}')
print()
print('')
for p in cadastro:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(k, v, end='')
print()




