sex = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while sex not in 'MF':
    sex = str(input('Dado inválido. Digite o seu sexo [M/F]: ')).upper()
print('Sexo {} selecionado com sucesso!' .format(sex))

