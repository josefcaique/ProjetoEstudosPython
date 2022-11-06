from datetime import datetime
inss = {'nome': str(input('Digite o nome: ')), 'idade': int(input('Digite o ano de nascimento: ')),
        'ctps': int(input('Carteira de trabalho (0 se n tiver): '))}
inss['idade'] = datetime.now().year - inss['idade']
if inss['ctps'] != 0:
    inss['contratação'] = int(input('Ano da contratação: '))
    inss['salario'] = float(input('Salário: R$ '))
    inss['aposentadoria'] = inss['idade'] + (35 - (datetime.now().year - inss['contratação']))
print('=-' * 20)
for k, v in inss.items():
    print(f'{k}: {v}')
