pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'O {k} é {v}')


#estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
#brasil = []
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]['UF'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla do estado: '))
    brasil.append(estado.copy)
print(brasil)

