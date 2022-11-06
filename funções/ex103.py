def ficha(txt='desconhecido', n=0):
    print(f'O jogador {txt} fez {n} gol(s) no campeonato')


nome = str(input('digite o nome do jogador: '))
gol = str(input('Digite o numero de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() in '':
    ficha(n=gol)
else:
    ficha(nome, gol)
