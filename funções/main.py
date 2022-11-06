def soma(*valores):
    s = 0
    for n in valores:
        print(n)


soma(2, 3)


def contador(*n):
    tam = len(n)
    print(f'Recebi os valores {n} e são {tam} números')


contador(7, 3, 1)
contador(1, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lista = [5, 3, 4, 9, 8]
dobra(lista)
print(lista)
