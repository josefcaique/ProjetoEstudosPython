jogador = dict()
gols = []
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Digite o número de partidas: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols foi o {c + 1} jogo? ')))
jogador['aproveitamento'] = gols[:]
jogador['total'] = sum(gols)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O {k} é {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for a, b in enumerate(jogador["aproveitamento"]):
    print(f'Na partida {a + 1}, fez {b} gols')
print(f'Foi um total de {jogador["total"]} gols')
print('=-' * 30)
