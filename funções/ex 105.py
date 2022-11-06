def notas(*n, sit=False):
    '''
    Cria um dicionario comsuas notas
    :param n: Digite os valores de "n" notas
    :param sit: Digite True para ver a situação ou deixe em branco para não
    :return: retorna o dicionario
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Otimo'
        elif r['media'] >= 5:
            r['situação'] = 'Bem mais ou menos'
        else:
            r['situação'] = 'Pessimo'
    return r


resp = notas(5.5, 2.5, 9, 1, 8.5, 10, sit=True)
print(resp)
help(notas)
