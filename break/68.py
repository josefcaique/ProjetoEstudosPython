from random import randint
print('Jogo do Impar ou Par')
c = 0
while True:
    pc = randint(1, 11)
    n = int(input('Selecione um número: '))
    s = n + pc
    poi = ' '
    while poi not in 'PI':
        poi = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'O computador colocou {pc} e você colocou {n} o resultado é {s}')
    print('DEU PAR' if s % 2 == 0 else 'DEU IMPAR, ', end='')
    if s % 2 == 0:
        if poi in 'Pp':
            print('Parabéns Você ganhou!')
        else:
            print('Que pena você errou!')
            break
    else:
        if poi in 'Pp':
            print('Que pena você errou!')
            break
        else:
            print('Parabéns Você ganhou!')
    print('Vamos jogar novamente...')
    c += 1
print('GAME OVER!')
print(f'Você ganhou {c} vezes')
