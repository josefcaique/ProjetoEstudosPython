ch = c18 = cm = 0
while True:
    ida = int(input('Digite a idade: '))
    sex = ' '
    while sex not in 'FM':
        sex = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    print('Pessoa cadastrada com sucesso!')
    if ida >= 18:
        c18 += 1
    if sex in 'Mm':
        ch += 1
    if sex == 'F' and ida < 20:
        cm += 1
    con = ' '
    while con not in 'SN':
        con = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if con in 'Nn':
        break
print(f'Tem {c18} pessoas menores de idade')
print(f'Tem {ch} homens cadastrados')
print(f'Tem {cm} mulheres com menos de 20 anos')
