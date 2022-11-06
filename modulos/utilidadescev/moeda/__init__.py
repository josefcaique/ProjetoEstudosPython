def moeda(n):
    a = str(n)
    a = f'R${n:>.2f}'.replace('.', ',')
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


def resumo(n=0, n1=10, n2=5):
    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metadedo preço: \t{metade(n,True)}')
    print(f'{n1}% de aumento: \t{aumentar(n, n1,True)}')
    print(f'{n2}% de desconto: \t{diminuir(n, n2,True)}')
    print('-' * 30)