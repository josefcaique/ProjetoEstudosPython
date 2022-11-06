jogador = dict()
gols = []
time = []
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Digite o número de partidas: '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols foi o {c + 1} jogo? ')))
    jogador['aproveitamento'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    while True:
        r = str(input('deseja continuar [S/N]? ')).upper()[0]
        if r in 'SN':
            break
        print('Erro, tente novamente!')
    if r == 'N':
        break
print('-' * 40)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for i, j in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Digite o valor da busca: '))
    if busca == 999:
        print('Programa encerrado!')
        break
    if busca >= len(time):
        print('Não existe jogador com esse código! ')
    else:
        print(f' Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["aproveitamento"]):
            print(f' No jogo {i + 1} fez {g} gols')


