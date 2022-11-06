from random import randint
from time import sleep
print('=-' * 30)
print(f'MEGA SENA')
print('=-' * 30)
jogo = []
r = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, r):
    jogo = [randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61),
            randint(1, 61)]
    jogo.sort()
    print(f'\033[0;32m Jogo {c + 1}: {jogo}\033[m')
    sleep(0.5)
    jogo.clear()
print('BOA SORTE')