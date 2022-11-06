listagem = ('Pão', 1.00, 'leite', 3.50, 'Frango', 10.90, 'Arroz', 5.00, 'Macarrão', 2.5)
print('-' * 35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-' * 35)
for cont in range(0, len(listagem)):
    if cont % 2 == 0:
        print(f'{listagem[cont]:.<30}', end='')
    else:
        print(f' R${listagem[cont]:>5}')
print('-' * 35)
