matriz = [[], [], []]
soma = somac = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input('Digite um valor: ')))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        # PAR
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        # Soma coluna
        if c == 2:
            somac += matriz[l][c]
        # Maior Linha 2
        if l == 1 and c == 0:
            mai = matriz[l][c]
        if l == 1 and mai < matriz[l][c]:
            mai = matriz[l][c]
        #Matriz
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares são {soma:^5}')
print(f'O maior valor da segunda linha é {mai:^5}')
print(f'A soma de todos da 3 coluna são {somac:^5}')
