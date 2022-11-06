def fatorial(n=1, s=False):
    '''
    -> Calcula o fatorial de um número
    :param n: O numero a ser calculado
    :param s:(opicional) Mostra ou não a conta, usar True ou False
    :return:O valor do fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if s:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
    return f


print(fatorial(9, True))
