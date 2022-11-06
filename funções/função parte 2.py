help(print)


def contador(i, f, p):
    """
    Hello, do a count and show on screen
    :param i:insert the start number
    :param f:insert the final number
    :param p:insert the step
    :return:
    """
    c = i
    while c <= f:
        print(c)
        c += p


contador(1, 10, 2)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r = somar(1, 2)
print(r)


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(a)


