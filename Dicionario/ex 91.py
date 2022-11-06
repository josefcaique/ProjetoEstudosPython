from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
jogos['jogador1'] = randint(1, 6)
jogos['jogador2'] = randint(1, 6)
jogos['jogador3'] = randint(1, 6)
jogos['jogador4'] = randint(1, 6)
ranking = list()
for k, v in jogos.items():
    print(f'o {k} tirou {v}')
    sleep(0.75)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('  == RANKING ==')
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}')
