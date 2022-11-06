def moeda(n):
    a = str(n)
    a = f'R${n}'.replace('.', ',')
    return a


def metade(n, resp=False):
    num = n / 2
    if resp:
        num = moeda(num)
    return num


def dobro(n, resp=False):
    num = n * 2
    if resp:
        num = moeda(num)
    return num


def aumentar(n, p, resp=False):
    num = n + ((n * p) / 100)
    if resp:
        num = moeda(num)
    return num


def diminuir(n, p, resp=False):
    num = n - ((n * p) / 100)
    if resp:
        num = moeda(num)
    return num


def resumo(n, n1, n2):
    print('-' * 30)
    print(f'{"Resumo do valor"}')
    print('-' * 30)
    print(f'Preço analisado: {moeda(n):^5}')
    print(f'Dobro do preço: {dobro(n, resp=True)}')
    print(f'Metadedo preço: {metade(n, resp=True)}')
    print(f'{n1}% de aumento: {aumentar(n, n1, resp=True)}')
    print(f'{n2}% de desconto: {diminuir(n, n2,resp=True)}')
    print('-' * 30)
