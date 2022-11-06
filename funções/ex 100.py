from random import randint


def sorteia(lista):
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
    print('PRONTO!')

def somapar(lista):
    print(f'Somando os valores pares de {lista}, temos: ', end='')
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(s)


numeros = list()
sorteia(numeros)
somapar(numeros)






